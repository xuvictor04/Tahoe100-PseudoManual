---
symbol: "SLC9A6"
type: "gene"
col: 12642
ensembl_id: "ENSG00000198689"
name: "solute carrier family 9 member A6"
location: "Xq26.3"
module: 30
arm: "+"
pooled_cpm: 22.73
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SLC9A6

*solute carrier family 9 member A6* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.26× (z +13.5, q 1e-38, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.560× (z -13.6, q 4e-39, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERAC1]] (+0.75, fdr 1e-05), [[SEC11A]] (+0.74, fdr 7e-06), [[MYPOP]] (+0.73, fdr 7e-06); moves opposite to [[NEPRO-AS1]] (-0.75, fdr 1e-05), [[WARS2-AS1]] (-0.74, fdr 1e-05), [[ERCC6L2]] (-0.72, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TTC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +13.5 | 1e-38 | 45/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +13.4 | 1e-38 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +11.3 | 3e-27 | 42/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +6.2 | 7e-08 | 27/46 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +5.9 | 5e-07 | 33/47 (PANC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.8 | 5e-07 | 25/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.1 | 0.003 | 19/46 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.013 | 19/47 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -13.6 | 4e-39 | 38/46 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -9.1 | 3e-17 | 32/46 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.629×** | -7.4 | 3e-11 | 27/47 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.662×** | -6.6 | 8e-09 | 18/31 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.716×** | -5.5 | 4e-06 | 21/40 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -5.4 | 6e-06 | 20/37 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -4.3 | 0.002 | 20/46 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -3.9 | 0.006 | 19/47 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.797×** | -3.7 | 0.011 | 12/47 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.070 | 16/47 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.832× | -3.0 | 0.13 | 14/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.8 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.9) |
| [[SW480 (line)]] | alt | 29.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.47 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -9.3) |
| [[A498 (line)]] | wt | 12.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[A549 (line)]] | wt | 23.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.347× (z -8.9) |
| [[C32 (line)]] | wt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -11.2) |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.8) |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 18.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.27× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.2) |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.9) |
| [[J82 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -14.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0894× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0789× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.8) |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0559× (z -14.0) |
| [[A-427 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERAC1]] | +0.75 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.74 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[MYPOP]] | +0.73 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[STRN]] | +0.71 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[NFRKB]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.70 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[UBAC1]] | +0.70 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[PLEKHH3]] | +0.70 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.70 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.70 | +0.69 / +0.39 | both halves | 5e-05 |  |
| [[ALG9]] | +0.70 | +0.77 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.75 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.74 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.72 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.71 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[LPXN]] | -0.70 | -0.74 / -0.42 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.70 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[TASOR]] | -0.70 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ST7L]] | -0.69 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[CYREN]] | -0.69 | -0.74 / -0.42 | both halves | 4e-05 |  |
| [[LINC00486]] | -0.69 | -0.73 / -0.38 | both halves | 6e-05 |  |
| [[MMADHC-DT]] | -0.68 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[ANGPT2]] | -0.68 | -0.67 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC6]] | B | TTC6 activity lowers SLC9A6's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without TTC6 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[DGKI]] | B | DGKI activity lowers SLC9A6's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.53× higher at baseline in the lines without DGKI | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SLC9A6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers SLC9A6's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without ZNF341-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ZHX2]] | B | ZHX2 activity lowers SLC9A6's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without ZHX2 | 0.087 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[GTF2H1]] | C | GTF2H1's natural level strengthens SLC9A6's drug response | GTF2H1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.06; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.835). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.2, -6.1); signed map (-36.8, -3.3). **Vector** length 104, 24.0% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.3 | +13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +13.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.5 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Esmolol (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:135,973,841-136,047,269 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NHE6, KIAA0267, NHE-6 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 6 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92581](https://www.uniprot.org/uniprotkb/Q92581) (Sodium/hydrogen exchanger 6):

> Endosomal Na(+), K(+)/H(+) antiporter. Mediates the electroneutral exchange of endosomal luminal H(+) for a cytosolic Na(+) or K(+). By facilitating proton efflux, SLC9A6 counteracts the acidity generated by vacuolar (V)-ATPase, thereby limiting luminal acidification. Responsible for alkalizing and maintaining the endosomal pH, and consequently in, e.g., endosome maturation and trafficking of recycling endosomal cargo. Plays a critical role during neurodevelopment by regulating synaptic …

**Summary**, from NCBI Gene [10479](https://www.ncbi.nlm.nih.gov/gene/10479):

> This gene encodes a sodium-hydrogen exchanger that is amember of the solute carrier family 9. The encoded protein localizes to early and recycling endosomes and may be involved in regulating endosomal pH and volume. Defects in this gene are associated with X-linked syndromic cognitive disability, Christianson type. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:11079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11079) · Entrez [10479](https://www.ncbi.nlm.nih.gov/gene/10479) · UniProt [Q92581](https://www.uniprot.org/uniprotkb/Q92581) · Ensembl [ENSG00000198689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198689)

## Data

Gene col 12642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12642); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12642]; `tensor/DDL_lfc|DDL_z.npy` [12642]; `embed/gene_vectors.npy` [12642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12642 or target_col == 12642). Every well: [[SLC9A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
