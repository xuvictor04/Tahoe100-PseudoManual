---
symbol: "DVL1"
type: "gene"
col: 2850
ensembl_id: "ENSG00000107404"
name: "dishevelled segment polarity protein 1"
location: "1p36.33"
module: 2
arm: "+"
pooled_cpm: 15.29
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DVL1

*dishevelled segment polarity protein 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +8.1, q 4e-13, up in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.42× (z +3.9, q 0.010, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.532× (z -9.9, q 3e-20, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNK2]] (+0.72, fdr 1e-05), [[ZNF598]] (+0.68, fdr 1e-05), [[R3HDM4]] (+0.68, fdr 2e-05); moves opposite to [[PNISR-AS1]] (-0.61, fdr 6e-05), [[HFE]] (-0.59, fdr 6e-05), [[VBP1]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BOK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.1 | 4e-13 | 32/37 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.1 | 3e-10 | 18/26 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.71×** | +6.0 | 4e-07 | 29/42 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.7 | 3e-04 | 21/34 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.010 | 14/44 (NCI-H1573, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.024 | 20/41 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +3.6 | 0.024 | 18/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.38×** | +3.5 | 0.024 | 20/45 (HCT15, LS 180, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +3.5 | 0.024 | 15/45 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.024 | 15/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.032 | 18/47 (CFPAC-1, A549, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.044 | 17/47 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.082 | 16/47 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.085 | 10/45 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -9.9 | 3e-20 | 38/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -6.7 | 4e-09 | 29/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.698×** | -5.6 | 3e-06 | 28/47 (A-427, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.009 | 21/45 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -3.9 | 0.011 | 23/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.028 | 17/47 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.497×** | -3.6 | 0.028 | 20/47 (NCI-H23, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -3.5 | 0.028 | 18/45 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.709×** | -3.4 | 0.050 | 11/47 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.055 | 16/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.1) |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.2) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -11.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -11.4) |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.1) |
| [[LoVo (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.0) |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0691× (z -8.6) |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.4) |
| [[SW480 (line)]] | alt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -11.6) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNK2]] | +0.72 | +0.68 / +0.49 | both halves | 1e-05 | same gene group |
| [[ZNF598]] | +0.68 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[R3HDM4]] | +0.68 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[GPSM1]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[STUB1]] | +0.66 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[TRABD]] | +0.65 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[PACS2]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PIP5K1C]] | +0.64 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[BRF1]] | +0.63 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[KIAA0930]] | +0.62 | +0.52 / +0.47 | both halves | 2e-05 | same gene group |
| [[UCKL1]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 | same gene group |
| [[FBRSL1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR-AS1]] | -0.61 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[HFE]] | -0.59 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[VBP1]] | -0.57 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TET2]] | -0.56 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[RBM48]] | -0.55 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[DECR1]] | -0.54 | -0.55 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[PHYH]] | -0.54 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[BTN3A3]] | -0.53 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[FAS]] | -0.53 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[PBLD]] | -0.53 | -0.48 / +0.02 | ⚠ not reproduced | 1.00 |  |
| [[C3orf38]] | -0.52 | -0.48 / -0.21 | both halves | 7e-04 |  |
| [[SNHG31]] | -0.52 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[PDHX]] | -0.52 | -0.39 / -0.31 | both halves | 2e-04 | same gene group |
| [[GIPC2]] | -0.52 | -0.49 / -0.25 | both halves | 4e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOK]] | B | BOK activity raises DVL1's level | lines that do not express BOK (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without BOK | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |
| [[TOP2A]] | B | TOP2A activity raises DVL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STX2]] | C | STX2 activity raises DVL1's level | lines that do not express STX2 (3) vs lines expressing it (47) | 1.40× lower at baseline in the lines without STX2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPW, PALS2, CAPRIN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.4, -3.6); signed map (-29.5, 2.7). **Vector** length 76.9, 16.8% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.4 | -5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.0 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | dishevelled segment polarity protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,335,276-1,349,418 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dishevelled segment polarity proteins; PDZ domain containing; MicroRNA protein coding host genes; DEP domain containing |
| Reactome | 17 pathways, smallest: Negative regulation of TCF-dependent signaling by DVL-interacting proteins; WNT mediated activation of DVL; Killing mechanisms |
| Matched by | ensembl_id |

**Function**, from UniProt [O14640](https://www.uniprot.org/uniprotkb/O14640) (Segment polarity protein dishevelled homolog DVL-1):

> Participates in Wnt signaling by binding to the cytoplasmic C-terminus of frizzled family members and transducing the Wnt signal to down-stream effectors. Plays a role both in canonical and non-canonical Wnt signaling. Plays a role in the signal transduction pathways mediated by multiple Wnt genes. Required for LEF1 activation upon WNT1 and WNT3A signaling. DVL1 and PAK1 form a ternary complex with MUSK which is important for MUSK-dependent regulation of AChR clustering during the formation of …

**Summary**, from NCBI Gene [1855](https://www.ncbi.nlm.nih.gov/gene/1855):

> DVL1, the human homolog of the Drosophila dishevelled gene (dsh) encodes a cytoplasmic phosphoprotein that regulates cell proliferation, acting as a transducer molecule for developmental processes, including segmentation and neuroblast specification. DVL1 is a candidate gene for neuroblastomatous transformation. The Schwartz-Jampel syndrome and Charcot-Marie-Tooth disease type 2A have been mapped to the same region as DVL1. The phenotypes of these diseases may be consistent with defects which …

**Accessions** — [HGNC:3084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3084) · Entrez [1855](https://www.ncbi.nlm.nih.gov/gene/1855) · UniProt [O14640](https://www.uniprot.org/uniprotkb/O14640) · Ensembl [ENSG00000107404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107404)

## Data

Gene col 2850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2850); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2850]; `tensor/DDL_lfc|DDL_z.npy` [2850]; `embed/gene_vectors.npy` [2850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2850 or target_col == 2850). Every well: [[DVL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DVL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
