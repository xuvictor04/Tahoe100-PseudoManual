---
symbol: "FRA10AC1"
type: "gene"
col: 7307
ensembl_id: "ENSG00000148690"
name: "FRA10A associated CGG repeat 1"
location: "10q23.33"
module: 12
arm: "+"
pooled_cpm: 67.59
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FRA10AC1

*FRA10A associated CGG repeat 1* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.37× (z +6.7, q 1e-08, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.679× (z -8.1, q 3e-13, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBMX2]] (+0.77, fdr 7e-06), [[NEMF]] (+0.75, fdr 7e-06), [[CEP290]] (+0.73, fdr 7e-06); moves opposite to [[HCFC1]] (-0.63, fdr 1e-05), [[SUMO3]] (-0.60, fdr 3e-05), [[EIF5A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +6.7 | 1e-08 | 33/48 (LS 180, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +6.3 | 1e-07 | 28/48 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +5.5 | 9e-06 | 28/48 (LS 180, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +5.3 | 1e-05 | 28/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.1 | 0.005 | 15/48 (AsPC-1, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.20×** | +3.8 | 0.016 | 21/48 (NCI-H1573, NCI-H2030, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | 1.17× | +3.4 | 0.059 | 21/49 (HT-29, A549, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.12× | +3.3 | 0.061 | 18/48 (NCI-H1573, NCI-H2030, …) | two highest doses | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.063 | 13/48 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.063 | 9/48 (LS 180, RKO, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.063 | 5/49 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | 1.31× | +3.0 | 0.12 | 10/48 (PANC-1, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -8.1 | 3e-13 | 36/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.692×** | -7.7 | 3e-12 | 33/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -7.3 | 6e-11 | 30/49 (A-172, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -6.9 | 5e-10 | 32/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.739×** | -6.3 | 3e-08 | 27/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.672×** | -4.4 | 0.001 | 25/48 (A-172, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.812×** | -4.4 | 0.001 | 22/48 (NCI-H460, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.694×** | -4.0 | 0.004 | 21/44 (SNU-423, Hs 766T, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.848× | -3.2 | 0.085 | 18/45 (H4, C-33 A, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -3.2 | 0.085 | 17/48 (SW480, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.085 | 12/49 (AN3 CA, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.859× | -3.1 | 0.11 | 17/48 (AN3 CA, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.8 | 0 | 8 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.359× (z -14.6) |
| [[SW480 (line)]] | alt | 57.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.312× (z -15.2) |
| [[HOP62 (line)]] | alt | 52.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.395× (z -10.5) |
| [[HT-29 (line)]] | alt | 54.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.390× (z -9.3) |
| [[LS 180 (line)]] | wt | 60.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -11.1) |
| [[H4 (line)]] | wt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0885× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 51.0 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.104× (z -8.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 87.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 81.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.9) ⚠ cell-cycle shift, explains ~79% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.0) |
| [[A-172 (line)]] | wt | 86.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -15.1) |
| [[AN3 CA (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -9.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C-33 A (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 80.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -13.0) |
| [[J82 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[KATO III (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 68.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.2) |
| [[PANC-1 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.544× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMX2]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[NEMF]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CEP290]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ZCCHC9]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CINP]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.71 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[RAD17]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZC3H15]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[RP9]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[NKAP]] | +0.69 | +0.74 / +0.69 | both halves | 7e-06 | STRING 637 |
| [[GTF2H2C]] | +0.68 | +0.74 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.60 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[EIF5A]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FRA10AC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises FRA10AC1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.8, -9.3); signed map (-17.0, -10.0). **Vector** length 111, 29.1% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | -0.9 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -4.7 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FRA10A associated CGG repeat 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:93,667,883-93,702,592 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C10orf4 |
| Gene groups (HGNC) | Spliceosomal C complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70Z53](https://www.uniprot.org/uniprotkb/Q70Z53) (Protein FRA10AC1):

> May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [118924](https://www.ncbi.nlm.nih.gov/gene/118924):

> The protein encoded by this gene is a nuclear phosphoprotein of unknown function. This gene contains a tandem CGG repeat region within a CpG island that normally consists of 8-14 repeats but can expand to over 200 repeats. The repeat region is within the 5' UTR of some transcript variants, but is intronic to another variant. The expanded repeat allele is a fragile site and becomes hypermethylated, causing a reduction in gene expression. A disease phenotype has not been associated with expanded …

**Accessions** — [HGNC:1162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1162) · Entrez [118924](https://www.ncbi.nlm.nih.gov/gene/118924) · UniProt [Q70Z53](https://www.uniprot.org/uniprotkb/Q70Z53) · Ensembl [ENSG00000148690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148690)

## Data

Gene col 7307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7307); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7307]; `tensor/DDL_lfc|DDL_z.npy` [7307]; `embed/gene_vectors.npy` [7307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7307 or target_col == 7307). Every well: [[FRA10AC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRA10AC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
