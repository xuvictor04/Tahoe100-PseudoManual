---
symbol: "SPESP1"
type: "gene"
col: 15107
ensembl_id: "ENSG00000258484"
name: "sperm equatorial segment protein 1"
location: "15q23"
module: 15
arm: "+"
pooled_cpm: 5.31
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SPESP1

*sperm equatorial segment protein 1* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.72× (z +30.3, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.658× (z -4.1, q 0.018, down in 14 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP14-AS1]] (+0.82, fdr 7e-06), [[INTS6-AS1]] (+0.80, fdr 7e-06), [[PRANCR]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.72×** | +30.3 | 0e+00 | 36/36 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +13.6 | 2e-39 | 31/35 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.26×** | +11.2 | 6e-27 | 31/37 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +9.5 | 2e-19 | 6/10 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.7 | 2e-12 | 16/24 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +6.8 | 1e-09 | 7/13 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.8 | 1e-09 | 23/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.7 | 9e-07 | 21/44 (HT-29, BT-474, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.4 | 7e-04 | 9/39 (J82, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 12/43 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.005 | 13/24 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.005 | 9/43 (A498, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.025 | 12/46 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.025 | 9/45 (RPMI-7951, HOP62, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.031 | 5/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.051 | 9/44 (A-172, A-427, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -4.1 | 0.018 | 14/44 (PANC-1, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -3.9 | 0.018 | 19/45 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.677×** | -3.9 | 0.018 | 13/47 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -3.8 | 0.018 | 12/44 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.716× | -3.3 | 0.10 | 6/47 (NCI-H661, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.704× | -3.3 | 0.10 | 13/42 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 5 µM |  | 0.715× | -3.2 | 0.11 | 5/44 (C-33 A, C32, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.545× | -3.1 | 0.12 | 11/36 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 2.80 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +11.8) | [[Trifluridine (drug)]] 0.5 µM 0.0536× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 3.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.27 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 20.3× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 4.79 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.50× (z +15.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -11.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW480 (line)]] | alt | 5.49 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +11.4) | — |
| [[A-172 (line)]] | wt | 5.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +12.8) | — |
| [[A498 (line)]] | wt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.5× (z +13.9) | — |
| [[A549 (line)]] | wt | 3.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 9.21 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0746× (z -8.7) |
| [[C32 (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 8.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.97× (z +15.2) | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 7.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.25× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 4.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.7) | — |
| [[J82 (line)]] | alt | 2.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +11.7) | — |
| [[KATO III (line)]] | alt | 5.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +10.8) | — |
| [[LoVo (line)]] | wt | 4.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 8.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 2.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.87× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.186× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 3.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 5.36 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0669× (z -8.8) |
| [[SNU-423 (line)]] | alt | 1.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.7× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +11.9) | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP14-AS1]] | +0.82 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.80 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[PRANCR]] | +0.80 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[SEC24B-AS1]] | +0.78 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[KLF3-AS1]] | +0.78 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[HLA-DMA]] | +0.78 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.77 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.77 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.77 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | +0.76 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.76 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.76 | +0.72 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPESP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02987]] | B | LINC02987 activity lowers SPESP1's level | lines that do not express LINC02987 (5) vs lines expressing it (45) | 1.34× higher at baseline in the lines without LINC02987 | 0.068 | ⚠ within organs, on part of the lines; also absent: NME4, ZNF566, SPIRE1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.7, 21.0); signed map (27.6, -6.7). **Vector** length 70.1, 11.7% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +30.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | sperm equatorial segment protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,818,221-68,946,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SP-ESP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UW49](https://www.uniprot.org/uniprotkb/Q6UW49) (Sperm equatorial segment protein 1):

> Involved in fertilization ability of sperm.

**Summary**, from NCBI Gene [246777](https://www.ncbi.nlm.nih.gov/gene/246777):

> The encoded protein is a human alloantigen involved in sperm-egg binding and fusion. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:15570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15570) · Entrez [246777](https://www.ncbi.nlm.nih.gov/gene/246777) · UniProt [Q6UW49](https://www.uniprot.org/uniprotkb/Q6UW49) · Ensembl [ENSG00000258484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258484)

## Data

Gene col 15107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15107); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15107]; `tensor/DDL_lfc|DDL_z.npy` [15107]; `embed/gene_vectors.npy` [15107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15107 or target_col == 15107). Every well: [[SPESP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPESP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
