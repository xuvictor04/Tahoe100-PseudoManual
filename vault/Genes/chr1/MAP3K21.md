---
symbol: "MAP3K21"
type: "gene"
col: 6789
ensembl_id: "ENSG00000143674"
name: "mitogen-activated protein kinase kinase kinase 21"
location: "1q42.2"
module: 77
arm: "+"
pooled_cpm: 44.85
n_lines_expressing: 39
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# MAP3K21

*mitogen-activated protein kinase kinase kinase 21* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.29× (z +7.9, q 2e-12, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.576× (z -11.6, q 4e-28, down in 21 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.750× (z -6.0, q 2e-07, down in 19 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPAT]] (+0.54, fdr 3e-05), [[FLVCR1]] (+0.54, fdr 3e-05), [[NT5DC3]] (+0.52, fdr 8e-05); moves opposite to [[TBCEL]] (-0.46, fdr 1e-04), [[CARD8]] (-0.46, fdr 1e-04), [[KCNMB2-AS1]] (-0.46, fdr 3e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CDS1]] → it (grade B ⚠); 2 go from it, the strongest it → [[HABP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +7.9 | 2e-12 | 22/37 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +6.4 | 5e-08 | 21/37 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +6.2 | 8e-08 | 18/37 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.9 | 6e-07 | 17/36 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.8 | 9e-07 | 14/37 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +5.5 | 4e-06 | 18/37 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/36 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 17/36 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.2 | 0.002 | 12/33 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 5 µM |  | 1.10× | +3.0 | 0.15 | 5/37 (SNU-423, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -11.6 | 4e-28 | 21/32 (LS 180, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.627×** | -10.2 | 8e-22 | 28/35 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.678×** | -7.8 | 1e-12 | 20/33 (SW48, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -7.6 | 5e-12 | 23/35 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.750×** | -6.0 | 2e-07 | 19/37 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.9 | 4e-07 | 19/37 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.674×** | -4.5 | 6e-04 | 17/38 (J82, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.834× | -3.9 | 0.006 | 15/37 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.835× | -3.9 | 0.006 | 10/37 (H4, J82, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -3.6 | 0.018 | 14/36 (A549, COLO 205, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.891× | -3.5 | 0.022 | 13/37 (Panc 03.27, SW1417, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -3.5 | 0.022 | 10/37 (A549, A498, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.854× | -3.4 | 0.027 | 6/37 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 0.867× | -3.1 | 0.078 | 11/35 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.868× | -3.1 | 0.078 | 7/38 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.868× | -3.1 | 0.078 | 6/37 (HOP62, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.3 | 11 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.76× (z +22.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.2) | — |
| [[SW480 (line)]] | alt | 60.8 | 7 (6 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.19× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.6 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.157× (z -16.3) |
| [[RKO (line)]] | wt | 55.6 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -16.7) |
| [[A498 (line)]] | wt | 80.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 138 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.342× (z -11.9) |
| [[LoVo (line)]] | wt | 104 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +9.0) ⚠ toxic | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -10.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.473× (z -9.4) |
| [[LS 180 (line)]] | wt | 71.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -20.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 14.5 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.47× (z +9.9) | — |
| [[SW48 (line)]] | wt | 90.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0641× (z -20.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.285× (z -9.7) |
| [[J82 (line)]] | alt | 39.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 44.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.37× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -8.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 57.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 77.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 76.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +17.0) | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 70.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.8) | — |
| [[AN3 CA (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPAT]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[FLVCR1]] | +0.54 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[NT5DC3]] | +0.52 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[SLC1A1]] | +0.51 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[RTN4R]] | +0.51 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[LONRF1]] | +0.51 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[PALS2]] | +0.50 | +0.43 / +0.48 | both halves | 3e-05 | same gene group |
| [[EEF2K]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[GARNL3]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[TMEM65]] | +0.48 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[ZYG11A]] | +0.47 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[SRD5A1]] | +0.47 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCEL]] | -0.46 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[CARD8]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[KCNMB2-AS1]] | -0.46 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[STAMBP]] | -0.45 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ZNF548]] | -0.44 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CHMP3]] | -0.44 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[CLHC1]] | -0.44 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ZNF655]] | -0.44 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[RGS5]] | -0.44 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[LINC01684]] | -0.44 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[TIGD6]] | -0.44 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[EXOC7]] | -0.43 | -0.37 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | CDS1 activity raises MAP3K21's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without CDS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[SLC29A2]] | B | SLC29A2 activity raises MAP3K21's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 3.03× lower at baseline in the lines without SLC29A2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity lowers MAP3K21's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HABP4]] | B | MAP3K21 activity lowers HABP4's level | lines that do not express MAP3K21 (11) vs lines expressing it (39) | 1.68× higher at baseline in the lines without MAP3K21 | 0.073 | ⚠ within organs, on part of the lines; also absent: PRSS16, KRT8, CHMP4C |
| [[TENT4B]] | B | MAP3K21 activity lowers TENT4B's level | lines that do not express MAP3K21 (11) vs lines expressing it (39) | 1.23× higher at baseline in the lines without MAP3K21 | 0.090 | ⚠ within organs, on part of the lines; also absent: PRSS16, KRT8, CHMP4C |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (18.7, -43.1); signed map (-49.0, -2.1). **Vector** length 87.0, 20.0% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:233,327,724-233,385,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1804, MLK4 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TCX8](https://www.uniprot.org/uniprotkb/Q5TCX8) (Mitogen-activated protein kinase kinase kinase 21):

> Negative regulator of TLR4 signaling. Does not activate JNK1/MAPK8 pathway, p38/MAPK14, nor ERK2/MAPK1 pathways.

**Summary**, from NCBI Gene [84451](https://www.ncbi.nlm.nih.gov/gene/84451):

> Predicted to enable JUN kinase kinase kinase activity and protein homodimerization activity. Predicted to be involved in protein phosphorylation and signal transduction. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29798) · Entrez [84451](https://www.ncbi.nlm.nih.gov/gene/84451) · UniProt [Q5TCX8](https://www.uniprot.org/uniprotkb/Q5TCX8) · Ensembl [ENSG00000143674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143674)

## Data

Gene col 6789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6789); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6789]; `tensor/DDL_lfc|DDL_z.npy` [6789]; `embed/gene_vectors.npy` [6789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6789 or target_col == 6789). Every well: [[MAP3K21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
