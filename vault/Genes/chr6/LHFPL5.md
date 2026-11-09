---
symbol: "LHFPL5"
type: "gene"
col: 12454
ensembl_id: "ENSG00000197753"
name: "LHFPL tetraspan subfamily member 5"
location: "6p21.31"
module: 90
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# LHFPL5

*LHFPL tetraspan subfamily member 5* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +9.9, q 4e-20, up in 15 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +4.8, q 3e-04, up in 13 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (HOP62 0.116×); [[Cobimetinib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0643×); [[Vilanterol (drug)]] 0.05 µM in 1 line (RKO 0.0732×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OMG]] (+0.67, fdr 7e-06), [[CNTNAP5]] (+0.65, fdr 1e-05), [[CNBD1]] (+0.64, fdr 1e-05); moves opposite to [[ZMYM3]] (-0.48, fdr 8e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C2CD4A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.9 | 4e-20 | 15/27 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.3 | 7e-11 | 4/10 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +5.1 | 8e-05 | 5/13 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 3e-04 | 13/38 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.7 | 3e-04 | 10/38 (J82, RPMI-7951, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.4 | 0.001 | 12/35 (NCI-H1792, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 6/37 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 7/44 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.56×** | +4.1 | 0.002 | 5/20 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.0 | 0.004 | 5/29 (A498, J82, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +3.9 | 0.006 | 9/46 (PANC-1, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.009 | 9/45 (KATO III, BT-474, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.019 | 5/31 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.024 | 6/43 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.032 | 4/44 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.049 | 4/43 (Hs 766T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.070 | 9/44 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12454.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (HOP62 0.116×); [[Cobimetinib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0643×); [[Vilanterol (drug)]] 0.05 µM in 1 line (RKO 0.0732×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -5.9 | 2e-06 | 11/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.773× | -3.1 | 0.49 | 4/44 (Hs 766T, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 4.09 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0643× (z -9.3) |
| [[HOP62 (line)]] | alt | 4.99 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.116× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 4.55 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.106× (z -8.9) |
| [[RKO (line)]] | wt | 5.01 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0732× (z -8.9) |
| [[A-172 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OMG]] | +0.67 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MAL2-AS1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PRKCA-AS1]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[VPS39-DT]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SCHLAP1]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[VENTXP1]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CLVS1]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM3]] | -0.48 | -0.37 / -0.47 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD4A]] | B | C2CD4A activity raises LHFPL5's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without C2CD4A | 0.032 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[CCDC39]] | C | CCDC39's natural level weakens LHFPL5's drug response | CCDC39's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.06; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | LHFPL5's natural level weakens CLVS1's drug response | LHFPL5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.58; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[KCNH1]] | C | LHFPL5's natural level weakens KCNH1's drug response | LHFPL5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.33; direction clear | 0.049 | ⚠ tissue can mimic it; precision caveat |
| [[SLC35F4]] | C | LHFPL5's natural level weakens SLC35F4's drug response | LHFPL5's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.73, reverse -0.59; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CHRM5]] | C | LHFPL5's natural level weakens CHRM5's drug response | LHFPL5's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.57; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.6, 30.4); signed map (33.4, 15.3). **Vector** length 37.5, 3.47% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -5.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | LHFPL tetraspan subfamily member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,797,206-35,845,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33835, dJ510O8.8, Tmhs; previously DFNB67 |
| Gene groups (HGNC) | LHFPL tetraspan proteins |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAF8](https://www.uniprot.org/uniprotkb/Q8TAF8) (LHFPL tetraspan subfamily member 5 protein):

> Auxiliary subunit of the mechanotransducer (MET) non-specific cation channel complex located at the tips of the shorter stereocilia of cochlear hair cells and that mediates sensory transduction in the auditory system. The MET complex is composed of two dimeric pore-forming ion-conducting transmembrane TMC (TMC1 or TMC2) subunits, and aided by several auxiliary proteins including LHFPL5, TMIE, CIB2/3 and TOMT, and the tip-link PCDH15. Functionally couples PCDH15 to the transduction channel.

**Summary**, from NCBI Gene [222662](https://www.ncbi.nlm.nih.gov/gene/222662):

> This gene is a member of the lipoma HMGIC fusion partner (LHFP) gene family, which is a subset of the superfamily of tetraspan transmembrane protein encoding genes. Mutations in this gene result in deafness in humans, and a mutation in a similar gene in mice results in deafness and vestibular dysfunction with severe degeneration of the organ of Corti. It is proposed to function in hair bundle morphogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21253) · Entrez [222662](https://www.ncbi.nlm.nih.gov/gene/222662) · UniProt [Q8TAF8](https://www.uniprot.org/uniprotkb/Q8TAF8) · Ensembl [ENSG00000197753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197753)

## Data

Gene col 12454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12454); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12454]; `tensor/DDL_lfc|DDL_z.npy` [12454]; `embed/gene_vectors.npy` [12454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12454 or target_col == 12454). Every well: [[LHFPL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHFPL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
