---
symbol: "ATP6V0A4"
type: "gene"
col: 2689
ensembl_id: "ENSG00000105929"
name: "ATPase H+ transporting V0 subunit a4"
location: "7q34"
module: 90
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# ATP6V0A4

*ATPase H+ transporting V0 subunit a4* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.79× (z +11.5, q 1e-27, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +8.0, q 3e-13, up in 8 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 2 lines (SHP-77 0.0625×, SK-MEL-2 0.189×); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.0998×, SK-MEL-2 0.188×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.119×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SHP-77 0.100×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP8A2]] (+0.64, fdr 1e-05), [[SLC35F4]] (+0.62, fdr 1e-05), [[GRIK1]] (+0.62, fdr 3e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OPRD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.79×** | +11.5 | 1e-27 | 1/1 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +10.4 | 7e-23 | 7/10 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +8.0 | 3e-13 | 8/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +7.8 | 9e-13 | 1/4 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.3 | 2e-08 | 10/25 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +6.0 | 2e-07 | 17/41 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.8 | 7e-07 | 2/9 (SK-MEL-2, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +4.7 | 2e-04 | 8/30 (A-172, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.3 | 0.001 | 3/15 (C32, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 1/42 (NCI-H2030) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 3/41 (PANC-1, A498, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +3.7 | 0.009 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.023 | 7/32 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +3.3 | 0.041 | 10/30 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.046 | 6/24 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.046 | 0/39 | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.046 | 1/16 (HEC-1-A) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.046 | 2/15 (SW1417, NCI-H2030) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2689.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 2 lines (SHP-77 0.0625×, SK-MEL-2 0.189×); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.0998×, SK-MEL-2 0.188×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.119×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SHP-77 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 0.694× | -3.3 | 0.31 | 9/41 (SK-MEL-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.784× | -3.1 | 0.31 | 8/44 (SHP-77, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.735× | -3.1 | 0.31 | 13/41 (SHP-77, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.694× | -3.1 | 0.31 | 8/44 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 8 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.188× (z -9.8) |
| [[J82 (line)]] | alt | 4.30 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0701× (z -9.8) |
| [[SW1417 (line)]] | alt | 4.44 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0644× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.766 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.867 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.813 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.726 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.927 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.613 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.900 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.738 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8A2]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 | pathway: Ion channel transport |
| [[SLC35F4]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[GRIK1]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[COL21A1]] | +0.62 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[XIRP2]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[DNAH2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MYT1L]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PECAM1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[IL19]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[PLB1]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SLC4A10]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OPRD1]] | B | OPRD1 activity raises ATP6V0A4's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without OPRD1 | 0.053 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[DNAH2]] | B | DNAH2 activity raises ATP6V0A4's level | lines that do not express DNAH2 (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without DNAH2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC4A8, NOTCH3, NFATC4; maybe low, not absent |
| [[MYH16]] | C | MYH16 activity lowers ATP6V0A4's level | lines that do not express MYH16 (3) vs lines expressing it (47) | 2.19× higher at baseline in the lines without MYH16 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARSD, PER3, IGF2BP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, 31.3); signed map (32.7, 17.9). **Vector** length 49.0, 6.36% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit a4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:138,706,294-138,799,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RDRTA2, VPP2, RTADR, a4, Vph1, Stv1; previously ATP6N1B, ATP6N2, RTA1C |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 9 pathways, smallest: Insulin receptor recycling; ROS and RNS production in phagocytes; Transferrin endocytosis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBG4](https://www.uniprot.org/uniprotkb/Q9HBG4) (V-type proton ATPase 116 kDa subunit a 4):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons (By similarity). V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment (By similarity). Involved in normal vectorial acid …

**Summary**, from NCBI Gene [50617](https://www.ncbi.nlm.nih.gov/gene/50617):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of intracellular compartments of eukaryotic cells. V-ATPase dependent acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:866) · Entrez [50617](https://www.ncbi.nlm.nih.gov/gene/50617) · UniProt [Q9HBG4](https://www.uniprot.org/uniprotkb/Q9HBG4) · Ensembl [ENSG00000105929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105929)

## Data

Gene col 2689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2689); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2689]; `tensor/DDL_lfc|DDL_z.npy` [2689]; `embed/gene_vectors.npy` [2689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2689 or target_col == 2689). Every well: [[ATP6V0A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
