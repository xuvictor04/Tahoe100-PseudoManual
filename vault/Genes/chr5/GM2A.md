---
symbol: "GM2A"
type: "gene"
col: 12277
ensembl_id: "ENSG00000196743"
name: "ganglioside GM2 activator"
location: "5q33.1"
module: 50
arm: "+"
pooled_cpm: 20.07
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 18
n_dd_up_clean: 21
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GM2A

*ganglioside GM2 activator* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.84× (z +15.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -19.1, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCYOX1]] (+0.74, fdr 7e-06), [[ASAH1]] (+0.72, fdr 7e-06), [[MOSPD3]] (+0.70, fdr 7e-06); moves opposite to [[NEPRO-AS1]] (-0.65, fdr 1e-05), [[NSRP1]] (-0.65, fdr 1e-05), [[ERCC4]] (-0.64, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RTL8C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.84×** | +15.4 | 0e+00 | 44/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.83×** | +15.3 | 0e+00 | 42/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +13.1 | 7e-37 | 38/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +12.7 | 1e-34 | 37/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +11.8 | 4e-30 | 40/48 (A-172, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +10.7 | 1e-24 | 31/46 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +10.4 | 3e-23 | 24/29 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +8.5 | 1e-15 | 35/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.61×** | +7.0 | 1e-10 | 33/48 (SW1417, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +7.0 | 2e-10 | 21/33 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.23×** | +6.2 | 3e-08 | 29/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +5.6 | 8e-07 | 23/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.3 | 4e-06 | 23/48 (BT-474, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 4e-05 | 20/47 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 5e-05 | 22/45 (J82, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 9/47 (CFPAC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.002 | 16/44 (A-427, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 7/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.011 | 15/48 (AsPC-1, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.400×** | -19.1 | 0e+00 | 42/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.302×** | -17.3 | 0e+00 | 42/46 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.397×** | -13.1 | 6e-37 | 40/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -10.4 | 4e-23 | 41/48 (NCI-H460, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -7.6 | 3e-12 | 34/48 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.620×** | -7.1 | 2e-10 | 34/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -6.1 | 8e-08 | 28/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.667×** | -6.0 | 2e-07 | 24/46 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.687×** | -5.5 | 2e-06 | 24/47 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.790×** | -4.9 | 5e-05 | 21/48 (A-427, NCI-H460, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.708×** | -4.9 | 5e-05 | 20/47 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.707×** | -4.8 | 6e-05 | 25/47 (SNU-423, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.601×** | -3.9 | 0.004 | 15/36 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.771×** | -3.8 | 0.005 | 16/48 (A549, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.767×** | -3.7 | 0.008 | 14/47 (SNU-423, LoVo, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.645×** | -3.4 | 0.024 | 15/47 (Hs 766T, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.1 | 5 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 4.26× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 18.4 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -19.0) |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 6.95× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.3) |
| [[LS 180 (line)]] | wt | 27.6 | 3 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +17.1) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 4.69× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -11.6) |
| [[A549 (line)]] | wt | 23.2 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.4) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0242× (z -45.8) |
| [[NCI-H2347 (line)]] | alt | 27.4 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.64× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.5) |
| [[SNU-423 (line)]] | alt | 32.3 | 1 | 3 | [[Selinexor (drug)]] 5 µM 2.25× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.3) |
| [[A498 (line)]] | wt | 13.1 | 2 | 1 | [[Selinexor (drug)]] 5 µM 2.38× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.84× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.5) |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.2) |
| [[KATO III (line)]] | alt | 8.01 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 7.47× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 31.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.0) |
| [[RKO (line)]] | wt | 9.66 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0646× (z -11.0) |
| [[SW1417 (line)]] | alt | 25.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +10.5) | — |
| [[SW480 (line)]] | alt | 7.59 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.93× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -8.6) |
| [[A-172 (line)]] | wt | 16.7 | 1 | 1 | [[Selinexor (drug)]] 5 µM 3.13× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.6) |
| [[A-427 (line)]] | wt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -16.5) |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0965× (z -9.2) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.115× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 17.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -9.1) |
| [[J82 (line)]] | alt | 13.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.42× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 9.44 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 19.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.36× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 19.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.03× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.9) |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.110× (z -9.0) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 7.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -10.1) |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0523× (z -11.9) |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -14.0) |
| [[LoVo (line)]] | wt | 9.40 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -8.9) |
| [[SW 900 (line)]] | alt | 9.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -8.9) |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYOX1]] | +0.74 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ASAH1]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 | pathway: Glycosphingolipid catabolism; STRING 505 |
| [[MOSPD3]] | +0.70 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FAM210B]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GRN]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ARSA]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism; STRING 483 |
| [[ITM2C]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TMED4]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[AP1S1]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.65 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SLC25A23]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.65 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.65 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[NME6]] | -0.62 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[DNAJC11]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[PSMD7]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.61 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ST7L]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TAF1]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[AFG3L1P]] | -0.61 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTL8C]] | B | RTL8C activity raises GM2A's level | lines that do not express RTL8C (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without RTL8C | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000286964, RTL8A, EHD3; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, -19.2); signed map (-51.1, -8.4). **Vector** length 99.3, 24.8% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.8 | +11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +15.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.8 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +15.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +13.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.7 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.2 | -17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.0 | -19.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | ganglioside GM2 activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,212,150-151,270,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAP-3, GM2-AP, GM2AP |
| Gene groups (HGNC) | MD-2 related lipid recognition domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 6 pathways, smallest: Glycosphingolipid catabolism; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P17900](https://www.uniprot.org/uniprotkb/P17900) (Ganglioside GM2 activator):

> Lipid-binding and transfer protein essential for lysosomal degradation of ganglioside GM2. Extracts single GM2 molecules from intralysosomal luminal vesicle (ILV) membranes and presents them in soluble form to beta-hexosaminidase A (HEXA) for cleavage of N-acetyl-D-galactosamine and conversion to GM3. Forms a stoichiometric GM2-GM2A complex that serves as the substrate for HEXA. Also stimulates the breakdown of glycolipid GA2 by HEXA (By similarity). Possesses dual function: membrane lipid …

**Summary**, from NCBI Gene [2760](https://www.ncbi.nlm.nih.gov/gene/2760):

> This gene encodes a small glycolipid transport protein which acts as a substrate specific co-factor for the lysosomal enzyme beta-hexosaminidase A. Beta-hexosaminidase A, together with GM2 ganglioside activator, catalyzes the degradation of the ganglioside GM2, and other molecules containing terminal N-acetyl hexosamines. Mutations in this gene result in GM2-gangliosidosis type AB or the AB variant of Tay-Sachs disease. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:4367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4367) · Entrez [2760](https://www.ncbi.nlm.nih.gov/gene/2760) · UniProt [P17900](https://www.uniprot.org/uniprotkb/P17900) · Ensembl [ENSG00000196743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196743)

## Data

Gene col 12277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12277); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12277]; `tensor/DDL_lfc|DDL_z.npy` [12277]; `embed/gene_vectors.npy` [12277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12277 or target_col == 12277). Every well: [[GM2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GM2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
