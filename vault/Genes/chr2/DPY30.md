---
symbol: "DPY30"
type: "gene"
col: 8606
ensembl_id: "ENSG00000162961"
name: "dpy-30 histone methyltransferase complex regulatory subunit"
location: "2p22.3"
module: 30
arm: "+"
pooled_cpm: 34.18
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# DPY30

*dpy-30 histone methyltransferase complex regulatory subunit* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +7.7, q 6e-12, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.68× (z +5.3, q 2e-05, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.461× (z -11.0, q 2e-25, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA12]] (+0.81, fdr 7e-06), [[DNAJC19]] (+0.77, fdr 1e-05), [[UNC45A]] (+0.76, fdr 7e-06); moves opposite to [[TUG1]] (-0.72, fdr 7e-06), [[CYREN]] (-0.69, fdr 1e-05), [[LINC01135]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[INAFM2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.7 | 6e-12 | 41/44 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.77×** | +5.6 | 8e-06 | 28/36 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 2e-05 | 35/48 (A549, BT-474, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.8 | 2e-04 | 35/47 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.4 | 0.002 | 28/48 (SK-MEL-2, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.52×** | +4.3 | 0.002 | 31/46 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.013 | 32/48 (RKO, J82, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.35× | +3.0 | 0.17 | 23/48 (LOX-IMVI, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -11.0 | 2e-25 | 46/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -5.7 | 3e-06 | 35/47 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -5.2 | 3e-05 | 35/48 (HepG2/C3A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -4.7 | 3e-04 | 36/48 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -4.6 | 4e-04 | 36/47 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -4.3 | 0.002 | 34/48 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.657×** | -4.2 | 0.002 | 33/48 (HepG2/C3A, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -4.2 | 0.002 | 34/48 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.733× | -3.1 | 0.11 | 22/48 (A-172, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -16.1) |
| [[PANC-1 (line)]] | alt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.5) |
| [[A498 (line)]] | wt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.5) |
| [[A549 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0849× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 47.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.6) |
| [[KATO III (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 48.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.2) |
| [[RKO (line)]] | wt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.0) |
| [[SNU-423 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.8) |
| [[SW480 (line)]] | alt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.0) |
| [[A-427 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA12]] | +0.81 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[DNAJC19]] | +0.77 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.76 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.72 | +0.69 / +0.57 | both halves | 8e-06 |  |
| [[POLR2I]] | +0.72 | +0.45 / +0.68 | both halves | 3e-05 | pathway: Activation of HOX genes during differentiation |
| [[MGST3]] | +0.71 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NBPF3]] | +0.70 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[RPP21]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[COMMD2]] | +0.69 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RBIS]] | +0.69 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[PCTP]] | +0.68 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[ATP5MJ]] | +0.68 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.72 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[CYREN]] | -0.69 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[LINC01135]] | -0.69 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SECISBP2]] | -0.68 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[CTBP1-DT]] | -0.66 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[PCBP1-AS1]] | -0.66 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PSMD6-AS1]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.66 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[MZF1-AS1]] | -0.66 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.66 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TENM3-AS1]] | -0.66 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.65 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAFM2]] | C | INAFM2 activity lowers DPY30's level | lines that do not express INAFM2 (4) vs lines expressing it (46) | 1.48× higher at baseline in the lines without INAFM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EXO5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.771). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.4, -5.8); signed map (-34.5, -3.8). **Vector** length 84.9, 25.3% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.0 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.7 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | dpy-30 histone methyltransferase complex regulatory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:31,867,809-32,039,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Saf19, HDPY-30, Cps25 |
| Gene groups (HGNC) | WRAD complex; DPY30 domain containing |
| Reactome | 30 pathways, smallest: Loss of Function of KMT2D in Kabuki Syndrome; Loss of Function of KMT2D in MLL4 Complex Formation in Kabuki Syndrome; Disorders of Developmental Biology |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C005](https://www.uniprot.org/uniprotkb/Q9C005) (Protein dpy-30 homolog):

> As part of the MLL1/MLL complex, involved in the methylation of histone H3 at 'Lys-4', particularly trimethylation. Histone H3 'Lys-4' methylation represents a specific tag for epigenetic transcriptional activation. May play some role in histone H3 acetylation. In a teratocarcinoma cell, plays a crucial role in retinoic acid-induced differentiation along the neural lineage, regulating gene induction and H3 'Lys-4' methylation at key developmental loci. May also play an indirect or direct role …

**Summary**, from NCBI Gene [84661](https://www.ncbi.nlm.nih.gov/gene/84661):

> This gene encodes an integral core subunit of the SET1/MLL family of H3K4 methyltransferases. The encoded protein directly controls cell cycle regulators and plays an important role in the proliferation and differentiation of human hematopoietic progenitor cells. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:24590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24590) · Entrez [84661](https://www.ncbi.nlm.nih.gov/gene/84661) · UniProt [Q9C005](https://www.uniprot.org/uniprotkb/Q9C005) · Ensembl [ENSG00000162961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162961)

## Data

Gene col 8606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8606); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8606]; `tensor/DDL_lfc|DDL_z.npy` [8606]; `embed/gene_vectors.npy` [8606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8606 or target_col == 8606). Every well: [[DPY30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
