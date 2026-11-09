---
symbol: "CHCHD10"
type: "gene"
col: 14696
ensembl_id: "ENSG00000250479"
name: "coiled-coil-helix-coiled-coil-helix domain containing 10"
location: "22q11.23"
module: 48
arm: "+"
pooled_cpm: 19.78
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# CHCHD10

*coiled-coil-helix-coiled-coil-helix domain containing 10* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.22× (z +8.0, q 1e-12, up in 35 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 8.64×, MIA PaCa-2 8.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -6.8, q 6e-09, down in 35 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MJ]] (+0.69, fdr 3e-05), [[TMEM256]] (+0.67, fdr 7e-06), [[COX7C]] (+0.67, fdr 1e-05); moves opposite to [[TUG1]] (-0.64, fdr 1e-05), [[SFPQ]] (-0.61, fdr 3e-05), [[HNRNPUL1]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TNFRSF10A-DT]] → it (grade B ⚠); 10 go from it, the strongest it → cells under [[Clotrimazole (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14696.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 8.64×, MIA PaCa-2 8.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.22×** | +8.0 | 1e-12 | 35/35 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.27×** | +6.8 | 4e-09 | 25/27 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.27×** | +4.5 | 0.001 | 24/30 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.90×** | +3.8 | 0.018 | 25/37 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -6.8 | 6e-09 | 35/41 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.469×** | -4.5 | 0.002 | 29/42 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.274×** | -4.0 | 0.012 | 33/42 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.316×** | -3.6 | 0.053 | 28/41 (HT-29, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.535×** | -3.5 | 0.057 | 25/42 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.341×** | -3.3 | 0.083 | 33/43 (LoVo, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.64× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -8.7) |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -8.6) |
| [[LoVo (line)]] | wt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.1) |
| [[RKO (line)]] | wt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -8.7) |
| [[A-172 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 10 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | +0.69 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[TMEM256]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[COX7C]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 | STRING 978 |
| [[ATP5MK]] | +0.67 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[ATP5PD]] | +0.66 | +0.42 / +0.68 | both halves | 4e-05 | STRING 508 |
| [[LAMTOR2]] | +0.65 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MHENCR]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[NENF]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.64 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[UQCRQ]] ⚠ | +0.64 | +0.46 / +0.65 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS; ⚠ in the vector space only through flagged drug-doses |
| [[COMTD1]] | +0.63 | +0.44 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.64 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.61 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[HNRNPUL1]] | -0.61 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[ZNF655]] | -0.59 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[SRCAP]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.58 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SRRM2]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SP2]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPL]] | -0.57 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[ERMAP]] | -0.56 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF10A-DT]] | B | TNFRSF10A-DT activity raises CHCHD10's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without TNFRSF10A-DT | 0.035 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |
| [[PCBD1]] | C | PCBD1 activity raises CHCHD10's level | lines that do not express PCBD1 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without PCBD1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FZD5, EZR, ZBED3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clotrimazole (drug)]] 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Clotrimazole 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.78× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs |
| cells under [[Aliskiren (drug)]] 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.71× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs |
| cells under [[Adenosine (drug)]] 5 µM | C | CHCHD10 activity raises the cells' numbers under Adenosine 5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.84× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs |
| cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.83× the cells of the other lines | 0.044 | ⚠ tissue-confounded; across organs |
| cells under [[Celecoxib (drug)]] 0.05 µM | C | CHCHD10 activity raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.74× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs |
| cells under [[Ixazomib (drug)]] 0.05 µM | C | CHCHD10 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.74× the cells of the other lines | 0.063 | ⚠ tissue-confounded; across organs |
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | C | CHCHD10 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 1.20× the cells of the other lines | 0.085 | ⚠ tissue-confounded; across organs |
| cells under [[Ritonavir (drug)]] 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.83× the cells of the other lines | 0.086 | ⚠ tissue-confounded; across organs |
| cells under [[Furosemide (drug)]] 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.82× the cells of the other lines | 0.089 | ⚠ tissue-confounded; across organs |
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | C | CHCHD10 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.77× the cells of the other lines | 0.0999 | ⚠ tissue-confounded; across organs |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.9, -19.1); signed map (-33.4, 7.1). **Vector** length 58.8, 15.9% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.52 to 31); *Respiratory electron transport* (reactome, mean cos +0.51 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.53 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -2.2 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -2.1 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,765,834-23,767,972 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N27C7-4, MIX17A; previously C22orf16 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYQ3](https://www.uniprot.org/uniprotkb/Q8WYQ3) (Coiled-coil-helix-coiled-coil-helix domain-containing protein 10, mitochondrial):

> May be involved in the maintenance of mitochondrial organization and mitochondrial cristae structure.

**Summary**, from NCBI Gene [400916](https://www.ncbi.nlm.nih.gov/gene/400916):

> This gene encodes a mitochondrial protein that is enriched at cristae junctions in the intermembrane space. It may play a role in cristae morphology maintenance or oxidative phosphorylation. Mutations in this gene cause frontotemporal dementia and/or amyotrophic lateral sclerosis-2. Alternative splicing of this gene results in multiple transcript variants. Related pseudogenes have been identified on chromosomes 7 and 19. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:15559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15559) · Entrez [400916](https://www.ncbi.nlm.nih.gov/gene/400916) · UniProt [Q8WYQ3](https://www.uniprot.org/uniprotkb/Q8WYQ3) · Ensembl [ENSG00000250479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250479)

## Data

Gene col 14696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14696); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14696]; `tensor/DDL_lfc|DDL_z.npy` [14696]; `embed/gene_vectors.npy` [14696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14696 or target_col == 14696). Every well: [[CHCHD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
