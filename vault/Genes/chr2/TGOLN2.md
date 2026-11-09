---
symbol: "TGOLN2"
type: "gene"
col: 7613
ensembl_id: "ENSG00000152291"
name: "trans-golgi network protein 2"
location: "2p11.2"
module: 25
arm: "+"
pooled_cpm: 98.25
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TGOLN2

*trans-golgi network protein 2* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.21× (z +14.4, q 2e-44, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.41× (z +6.4, q 2e-08, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.614× (z -12.2, q 1e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMGT1]] (+0.79, fdr 7e-06), [[TMX1]] (+0.77, fdr 7e-06), [[AP2M1]] (+0.75, fdr 7e-06); moves opposite to [[SNHG8]] (-0.76, fdr 7e-06), [[SNHG32]] (-0.73, fdr 7e-06), [[NSUN5P2-1]] (-0.68, fdr 7e-06, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[EPB41L4A-AS1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOTAIRM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +14.4 | 2e-44 | 43/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +13.4 | 1e-38 | 47/49 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +8.6 | 1e-15 | 34/45 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.4 | 2e-08 | 37/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +6.3 | 3e-08 | 39/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.7 | 1e-06 | 33/48 (A549, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +4.4 | 8e-04 | 26/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.25×** | +4.3 | 0.001 | 28/48 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.012 | 21/48 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.064 | 18/49 (A-172, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.18× | +3.2 | 0.074 | 20/48 (PANC-1, NCI-H2030, …) | top dose only | composition shift |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.089 | 14/49 (PANC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -12.2 | 1e-31 | 40/48 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.662×** | -7.5 | 2e-11 | 40/49 (J82, A549, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.689×** | -7.1 | 3e-10 | 34/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -5.9 | 4e-07 | 30/49 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.013 | 23/48 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Penfluridol (drug)]] 5 µM |  | **0.821×** | -3.6 | 0.029 | 21/47 (A498, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.762×** | -3.5 | 0.042 | 24/48 (Panc 03.27, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.864× | -3.3 | 0.063 | 13/49 (CFPAC-1, RKO, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.842× | -3.3 | 0.069 | 18/49 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 5 µM |  | 0.853× | -3.0 | 0.15 | 9/49 (HCT15, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 78.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.30× (z +9.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.444× (z -9.6) |
| [[HOP62 (line)]] | alt | 123 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.9) |
| [[NCI-H596 (line)]] | alt | 75.5 | 1 | 3 (1 ⚠) | [[Atazanavir (sulfate) (drug)]] 0.05 µM 2.15× (z +12.1) | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.191× (z -27.2) |
| [[PANC-1 (line)]] | alt | 152 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +16.7) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.507× (z -9.1) |
| [[SNU-423 (line)]] | alt | 82.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +14.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.457× (z -8.7) |
| [[A-172 (line)]] | wt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 171 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 101 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +12.0) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.441× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 108 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.2) |
| [[C-33 A (line)]] | alt | 85.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.2) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.269× (z -11.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 93.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.2) |
| [[H4 (line)]] | wt | 122 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 176 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -20.9) |
| [[HS-578T (line)]] | alt | 76.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +12.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 91.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 93.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.7) |
| [[C32 (line)]] | wt | 82.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +12.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 118 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 74.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 92.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.4) |
| [[Hs 766T (line)]] | wt | 77.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.9) |
| [[HT-29 (line)]] | alt | 122 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.5) |
| [[J82 (line)]] | alt | 86.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.395× (z -9.9) |
| [[KATO III (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 93.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.9) |
| [[SHP-77 (line)]] | alt | 57.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 74.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.111× (z -8.6) |
| [[SW 900 (line)]] | alt | 100.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.1) |
| [[AN3 CA (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 82.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMGT1]] | +0.79 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[TMX1]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 | pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 988 |
| [[TMEM30A]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[VAMP3]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 | pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 841 |
| [[NONO]] | +0.69 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.68 | +0.48 / +0.82 | both halves | 2e-05 |  |
| [[GTF3C1]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[PPT1]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TAF6]] | +0.67 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[NAGA]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | STRING 548 |

## Genes that move opposite

*30 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG8]] | -0.76 | -0.77 / -0.72 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.73 | -0.71 / -0.69 | both halves | 7e-06 |  |
| [[NSUN5P2-1]] ⚠ | -0.68 | -0.63 / -0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | -0.67 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | -0.66 | -0.62 / -0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG12]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ADPRM]] | -0.65 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.65 | -0.54 / -0.78 | both halves | 1e-05 |  |
| [[NSUN5P1-1]] | -0.65 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.64 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 | STRING 414 |
| [[SNHG6]] | -0.63 | -0.64 / -0.73 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.63 | -0.41 / -0.75 | both halves | 4e-05 |  |
| [[SNHG7]] | -0.62 | -0.59 / -0.70 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOTAIRM1]] | B | HOTAIRM1 activity raises TGOLN2's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without HOTAIRM1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |
| [[HDAC6]] | B | HDAC6 activity lowers TGOLN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.4, -22.2); signed map (-21.0, -37.5). **Vector** length 131, 38.5% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.2 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.5 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.8 | +6.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +4.2 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.4 | +3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +3.1 | +2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +3.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -7.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -5.3 | -7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.1 | -3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.4 | -2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.8 | -2.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | trans-golgi network protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,318,027-85,328,251 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TGN51, TGN46, TGN48, TGN38, TTGN2 |
| Reactome | 10 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [O43493](https://www.uniprot.org/uniprotkb/O43493) (Trans-Golgi network integral membrane protein 2):

> May be involved in regulating membrane traffic to and from trans-Golgi network.

**Summary**, from NCBI Gene [10618](https://www.ncbi.nlm.nih.gov/gene/10618):

> This gene encodes a type I integral membrane protein that is localized to the trans-Golgi network, a major sorting station for secretory and membrane proteins. The encoded protein cycles between early endosomes and the trans-Golgi network, and may play a role in exocytic vesicle formation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:15450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15450) · Entrez [10618](https://www.ncbi.nlm.nih.gov/gene/10618) · UniProt [O43493](https://www.uniprot.org/uniprotkb/O43493) · Ensembl [ENSG00000152291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152291)

## Data

Gene col 7613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7613); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7613]; `tensor/DDL_lfc|DDL_z.npy` [7613]; `embed/gene_vectors.npy` [7613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7613 or target_col == 7613). Every well: [[TGOLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGOLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
