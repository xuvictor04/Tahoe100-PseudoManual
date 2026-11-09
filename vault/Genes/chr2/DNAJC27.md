---
symbol: "DNAJC27"
type: "gene"
col: 3626
ensembl_id: "ENSG00000115137"
name: "DnaJ heat shock protein family (Hsp40) member C27"
location: "2p23.3"
module: 130
arm: "+"
pooled_cpm: 15.14
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# DNAJC27

*DnaJ heat shock protein family (Hsp40) member C27* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +14.0, q 1e-41, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.528× (z -11.2, q 1e-26, down in 19 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.633× (z -8.4, q 2e-14, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 0.180×, HOP62 0.241×, HCT15 0.142×, SNU-423 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HCT15 0.122×, RPMI-7951 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.213×, NCI-H460 0.337×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0531×); [[Peretinoin (drug)]] 0.5 µM in 1 line (H4 0.0618×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.103×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DICER1-AS1]] (+0.71, fdr 7e-06), [[PIGP]] (+0.70, fdr 1e-05), [[OSCP1]] (+0.67, fdr 7e-06); moves opposite to [[ACOT7]] (-0.64, fdr 1e-05), [[USB1]] (-0.63, fdr 1e-05), [[GATAD2A]] (-0.63, fdr 7e-06).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GIHCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +14.0 | 1e-41 | 34/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +13.8 | 4e-41 | 36/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +10.1 | 8e-22 | 28/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +7.5 | 8e-12 | 22/48 (J82, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.4 | 2e-08 | 25/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.1 | 3e-05 | 20/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.8 | 2e-04 | 19/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.2 | 0.002 | 12/46 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +4.1 | 0.002 | 8/48 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.003 | 15/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.16× | +3.7 | 0.010 | 7/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.7 | 0.010 | 5/48 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.20× | +3.6 | 0.012 | 7/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3626.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 0.180×, HOP62 0.241×, HCT15 0.142×, SNU-423 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HCT15 0.122×, RPMI-7951 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.213×, NCI-H460 0.337×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0531×); [[Peretinoin (drug)]] 0.5 µM in 1 line (H4 0.0618×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -11.2 | 1e-26 | 19/28 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.633×** | -8.4 | 2e-14 | 27/47 (NCI-H661, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.691×** | -6.8 | 2e-09 | 22/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.699×** | -6.6 | 8e-09 | 22/42 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.699×** | -6.1 | 1e-07 | 14/35 (HCT15, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.754×** | -5.2 | 2e-05 | 16/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.796×** | -4.2 | 0.002 | 10/48 (SW480, SHP-77, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.818×** | -3.7 | 0.017 | 12/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.813×** | -3.6 | 0.017 | 14/43 (SNU-1, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.874× | -3.3 | 0.047 | 12/48 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.834× | -3.3 | 0.047 | 3/48 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.842× | -3.2 | 0.075 | 10/48 (HS-578T, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.1 | 0.075 | 12/48 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.075 | 7/47 (H4, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 17.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 20.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.74× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.315× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0531× (z -11.1) |
| [[H4 (line)]] | wt | 12.5 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0618× (z -10.5) |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.20 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0980× (z -9.5) |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -13.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.103× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.5) | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0761× (z -9.8) |
| [[A-172 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DICER1-AS1]] | +0.71 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PIGP]] | +0.70 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[OSCP1]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ASTE1]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ZNF821]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CDKN1B]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.64 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[SPACA9]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT7]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[USB1]] | -0.63 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.63 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[LRP8]] | -0.62 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[CMIP]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ARHGAP8]] | -0.61 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ASAP2]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[CAP1]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ACTN1]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[MTAP]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GIHCG]] | B | GIHCG activity raises DNAJC27's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without GIHCG | 0.006 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises DNAJC27's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.0, 13.7); signed map (-8.0, -0.3). **Vector** length 80.9, 14.5% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.7 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.6 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.1 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,943,636-24,972,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RabJS; previously RBJ |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZQ0](https://www.uniprot.org/uniprotkb/Q9NZQ0) (DnaJ homolog subfamily C member 27):

> GTPase which can activate the MEK/ERK pathway and induce cell transformation when overexpressed. May act as a nuclear scaffold for MAPK1, probably by association with MAPK1 nuclear export signal leading to enhanced ERK1/ERK2 signaling.

**Summary**, from NCBI Gene [51277](https://www.ncbi.nlm.nih.gov/gene/51277):

> Predicted to enable GTPase activity. Predicted to be involved in intracellular protein transport. Predicted to be located in cytoplasmic vesicle and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30290) · Entrez [51277](https://www.ncbi.nlm.nih.gov/gene/51277) · UniProt [Q9NZQ0](https://www.uniprot.org/uniprotkb/Q9NZQ0) · Ensembl [ENSG00000115137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115137)

## Data

Gene col 3626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3626); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3626]; `tensor/DDL_lfc|DDL_z.npy` [3626]; `embed/gene_vectors.npy` [3626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3626 or target_col == 3626). Every well: [[DNAJC27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
