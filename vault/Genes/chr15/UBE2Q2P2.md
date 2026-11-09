---
symbol: "UBE2Q2P2"
type: "gene"
col: 15199
ensembl_id: "ENSG00000259429"
name: "UBE2Q2 pseudogene 2"
location: "15q25.2"
module: 99
arm: "+"
pooled_cpm: 67.33
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 23
n_dd_up_clean: 21
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# UBE2Q2P2

*UBE2Q2 pseudogene 2* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.73× (z +10.3, q 5e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.520× (z -12.2, q 1e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P2-1]] (+0.90, fdr 7e-06, ⚠ same locus), [[GPT2]] (+0.72, fdr 7e-06), [[GOLGA6L9]] (+0.71, fdr 1e-05, ⚠ same locus), [[TPD52]] (+0.71, fdr 1e-05), [[CDON]] (+0.69, fdr 7e-06); moves opposite to [[CFLAR]] (-0.61, fdr 2e-05), [[C6orf120]] (-0.61, fdr 1e-05), [[ZC3H4]] (-0.61, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EPIC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +10.3 | 5e-22 | 38/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +10.0 | 4e-21 | 39/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +9.5 | 5e-19 | 36/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +8.8 | 2e-16 | 38/48 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.9 | 8e-10 | 34/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.5 | 1e-08 | 26/48 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.25×** | +5.8 | 5e-07 | 25/48 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.8 | 5e-07 | 32/44 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.4 | 4e-06 | 26/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 1e-05 | 30/49 (MIA PaCa-2, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +5.2 | 1e-05 | 28/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +5.0 | 3e-05 | 33/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 26/48 (A498, COLO 205, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **1.29×** | +4.6 | 2e-04 | 28/48 (NCI-H1792, C32, …) | rises with dose | plate-row cell shift; position effect removed |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.4 | 5e-04 | 23/49 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 8e-04 | 22/49 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.001 | 24/47 (SNU-1, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -12.2 | 1e-31 | 40/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -12.0 | 1e-30 | 42/49 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -10.9 | 1e-25 | 32/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -10.2 | 2e-22 | 35/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -9.0 | 4e-17 | 41/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.599×** | -8.9 | 7e-17 | 33/45 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.621×** | -8.6 | 8e-16 | 41/47 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -7.8 | 4e-13 | 29/43 (SK-MEL-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.742×** | -7.5 | 3e-12 | 35/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.673×** | -7.4 | 8e-12 | 33/49 (NCI-H1792, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.680×** | -7.2 | 3e-11 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -6.5 | 3e-09 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.516×** | -6.5 | 5e-09 | 29/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -5.9 | 1e-07 | 30/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.761×** | -5.1 | 1e-05 | 26/47 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.695×** | -4.8 | 5e-05 | 26/47 (AN3 CA, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.623×** | -4.6 | 1e-04 | 27/45 (RPMI-7951, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.632×** | -4.5 | 2e-04 | 23/48 (LOX-IMVI, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.779×** | -4.3 | 5e-04 | 24/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.796×** | -4.0 | 0.002 | 21/47 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.003 | 19/48 (LoVo, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 131 | 2 (1 ⚠) | 10 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.65× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -20.5) |
| [[LoVo (line)]] | wt | 164 | 1 | 9 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.64× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -18.0) |
| [[C32 (line)]] | wt | 71.3 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 61.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -15.8) |
| [[SNU-1 (line)]] | wt | 106 | 2 | 5 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.08× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0780× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.256× (z -12.1) |
| [[A498 (line)]] | wt | 57.6 | 2 | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.365× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 94.2 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.425× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 49.7 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 2.60× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.8) |
| [[SW480 (line)]] | alt | 53.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 155 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.1) |
| [[HT-29 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 2 | 1 | [[Bortezomib (drug)]] 0.05 µM 3.45× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -13.7) |
| [[SW48 (line)]] | wt | 128 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.353× (z -9.2) |
| [[A-172 (line)]] | wt | 49.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 24.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 57.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0714× (z -18.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 46.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 41.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 51.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.445× (z -9.8) |
| [[A-427 (line)]] | wt | 54.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.498× (z -9.0) |
| [[A549 (line)]] | wt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.9) |
| [[CHP-212 (line)]] | wt | 61.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -10.3) |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.6) |
| [[KATO III (line)]] | alt | 67.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 48.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.2) |
| [[RKO (line)]] | wt | 94.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -10.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 68.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.8) |
| [[SW 1271 (line)]] | alt | 99.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -8.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -15.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P2-1]] | +0.90 | +0.90 / +0.85 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GPT2]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[GOLGA6L9]] | +0.71 | +0.52 / +0.71 | both halves | 1e-05 | ⚠ same locus (9.7 kb, same strand: neighbours can correlate without regulation) |
| [[TPD52]] | +0.71 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CDON]] | +0.69 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GARS1]] | +0.67 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[HSPA5]] | +0.67 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[BCKDHB]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[HACE1]] | +0.66 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[GFPT1]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PDK3]] | +0.63 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CLGN]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFLAR]] | -0.61 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[C6orf120]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.61 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[INO80D]] | -0.60 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | -0.60 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[ZNF747]] | -0.60 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[CTBP1-DT]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TRMT5]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | -0.59 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[FAM200A]] | -0.58 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[TUG1]] | -0.58 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[ZNF543]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPIC1]] | B | EPIC1 activity raises UBE2Q2P2's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without EPIC1 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[HSPA12A]] | C | HSPA12A activity raises UBE2Q2P2's level | lines that do not express HSPA12A (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without HSPA12A | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR3659HG, ENSG00000287400; maybe low, not absent |
| [[AGTPBP1]] | C | AGTPBP1 activity raises UBE2Q2P2's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without AGTPBP1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.2, -14.6); signed map (-36.6, 20.0). **Vector** length 139, 43.9% of its response variance represented; |z| ≥ 3 in 1,382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.8 | +9.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.4 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.8 | +5.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.9 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.1 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | UBE2Q2 pseudogene 2 |
| Locus type | pseudogene |
| Location | 15q25.2 — chr15:82,391,844-82,420,075 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously UBE2QP2, UBE2Q2P3 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37440) · Entrez [100134869](https://www.ncbi.nlm.nih.gov/gene/100134869) · Ensembl [ENSG00000259429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259429)

## Data

Gene col 15199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15199); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15199]; `tensor/DDL_lfc|DDL_z.npy` [15199]; `embed/gene_vectors.npy` [15199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15199 or target_col == 15199). Every well: [[UBE2Q2P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q2P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
