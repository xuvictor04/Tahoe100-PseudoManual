---
symbol: "CDH24"
type: "gene"
col: 6352
ensembl_id: "ENSG00000139880"
name: "cadherin 24"
location: "14q11.2"
module: 126
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# CDH24

*cadherin 24* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.99× (z +11.9, q 4e-30, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +7.7, q 2e-12, up in 15 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.611× (z -4.5, q 0.005, down in 10 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (LS 180 0.0829×); [[Neratinib (drug)]] 0.05 µM in 1 line (SW480 0.0650×); [[GSK1059615 (drug)]] 0.05 µM in 1 line (NCI-H460 0.0612×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY6]] (+0.67, fdr 1e-05), [[HCN3]] (+0.61, fdr 7e-06), [[ADGRB2]] (+0.60, fdr 7e-06); moves opposite to [[ZNF696]] (-0.53, fdr 3e-05), [[NIFK]] (-0.52, fdr 3e-05), [[MRPS18B]] (-0.50, fdr 4e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +11.9 | 4e-30 | 4/4 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +11.8 | 1e-29 | 12/16 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +10.0 | 3e-21 | 4/6 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +7.7 | 2e-12 | 15/33 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.89×** | +5.5 | 5e-06 | 7/13 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.70×** | +4.8 | 2e-04 | 13/45 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 4e-04 | 11/38 (A498, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.4 | 7e-04 | 9/34 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.002 | 9/31 (Hs 766T, SHP-77, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 5/44 (RKO, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 9/43 (NCI-H2347, HEC-1-A, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.60×** | +4.0 | 0.003 | 4/29 (NCI-H460, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.57×** | +3.9 | 0.005 | 5/33 (LS 180, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.8 | 0.006 | 2/23 (PANC-1, MIA PaCa-2) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.8 | 0.006 | 5/17 (NCI-H2347, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.018 | 5/45 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Captopril (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.061 | 1/43 (NCI-H460) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.073 | 4/19 (LoVo, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.088 | 2/44 (HEC-1-A, C-33 A) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6352.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (LS 180 0.0829×); [[Neratinib (drug)]] 0.05 µM in 1 line (SW480 0.0650×); [[GSK1059615 (drug)]] 0.05 µM in 1 line (NCI-H460 0.0612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -4.5 | 0.005 | 10/43 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.694× | -3.3 | 0.27 | 9/45 (C32, C-33 A, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.707× | -3.1 | 0.31 | 10/45 (A-172, SW48, …) | inconsistent across doses | position effect removed |
| [[Adenosine (drug)]] 0.5 µM |  | 0.717× | -3.0 | 0.32 | 2/42 (NCI-H1792, NCI-H1573) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 6.00 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0829× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.05 µM 0.0612× (z -9.0) |
| [[SW480 (line)]] | alt | 1.82 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0650× (z -9.7) |
| [[A-172 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY6]] | +0.67 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[HCN3]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ADGRB2]] | +0.60 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[TP53I11]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.58 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[OTUD3]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FRMPD3]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[C4orf46]] | +0.56 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[MAN2A2]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SEPTIN8]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[RAB15]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MICB]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF696]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NIFK]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MRPS18B]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DDX27]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[NOL7]] ⚠ | -0.48 | -0.48 / -0.39 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TATDN1]] | -0.48 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[MECR]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[SETX]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[FCF1]] | -0.47 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[RSPH3]] | -0.47 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[REXO4]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[SURF6]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DDX18]] | -0.46 | -0.40 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDH24's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GPC4]] | B | GPC4 activity raises CDH24's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without GPC4 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |
| [[GAS6]] | B | GAS6 activity raises CDH24's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without GAS6 | 0.096 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.7, -23.1); signed map (0.2, 6.3). **Vector** length 48.9, 5.95% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | -1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | +0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,047,062-23,057,538 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDH11L |
| Gene groups (HGNC) | Type II classical cadherins |
| Reactome | 9 pathways, smallest: CDH11 homotypic and heterotypic interactions; Regulation of CDH11 function; Regulation of CDH11 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UP0](https://www.uniprot.org/uniprotkb/Q86UP0) (Cadherin-24):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. Cadherin-24 mediate strong cell-cell adhesion.

**Summary**, from NCBI Gene [64403](https://www.ncbi.nlm.nih.gov/gene/64403):

> Enables several functions, including alpha-catenin binding activity; beta-catenin binding activity; and delta-catenin binding activity. Acts upstream of or within cell-cell adhesion. Located in cell-cell junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14265) · Entrez [64403](https://www.ncbi.nlm.nih.gov/gene/64403) · UniProt [Q86UP0](https://www.uniprot.org/uniprotkb/Q86UP0) · Ensembl [ENSG00000139880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139880)

## Data

Gene col 6352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6352); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6352]; `tensor/DDL_lfc|DDL_z.npy` [6352]; `embed/gene_vectors.npy` [6352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6352 or target_col == 6352). Every well: [[CDH24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
