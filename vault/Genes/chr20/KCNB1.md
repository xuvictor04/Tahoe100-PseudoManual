---
symbol: "KCNB1"
type: "gene"
col: 8162
ensembl_id: "ENSG00000158445"
name: "potassium voltage-gated channel subfamily B member 1"
location: "20q13.13"
module: 140
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 37
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# KCNB1

*potassium voltage-gated channel subfamily B member 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.0× (z +31.4, q 0e+00, up in 24 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Acetazolamide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0740×); [[Dexmedetomidine (drug)]] 5 µM in 1 line (NCI-H2030 0.0699×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUX2]] (+0.68, fdr 7e-06), [[RTN4RL1]] (+0.66, fdr 9e-06), [[EFHD1]] (+0.66, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.0×** | +31.4 | 0e+00 | 24/25 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.72×** | +16.6 | 0e+00 | 23/28 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.11×** | +16.2 | 0e+00 | 36/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.84×** | +15.2 | 0e+00 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.18×** | +14.6 | 0e+00 | 30/41 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.07×** | +14.5 | 1e-45 | 6/9 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.30×** | +13.0 | 6e-37 | 33/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +11.5 | 9e-29 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.95×** | +9.7 | 3e-20 | 26/39 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.88×** | +9.5 | 2e-19 | 22/31 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +8.6 | 3e-16 | 25/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.2 | 9e-15 | 11/41 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +8.0 | 4e-14 | 12/29 (C32, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +7.3 | 1e-11 | 5/8 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +7.0 | 1e-10 | 10/25 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.05×** | +6.4 | 5e-09 | 12/37 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.2 | 2e-08 | 8/22 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.7 | 5e-07 | 7/27 (A549, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +5.2 | 6e-06 | 9/33 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Acetazolamide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0740×); [[Dexmedetomidine (drug)]] 5 µM in 1 line (NCI-H2030 0.0699×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 2.88 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 64.3× (z +10.0) | — |
| [[C32 (line)]] | wt | 1.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 3.59 | 0 | 2 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0740× (z -8.6) |
| [[PANC-1 (line)]] | alt | 1.77 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 16.5× (z +8.7) | — |
| [[SW480 (line)]] | alt | 2.00 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +11.2) | — |
| [[A-172 (line)]] | wt | 1.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +9.0) | — |
| [[A498 (line)]] | wt | 1.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +10.1) | — |
| [[A549 (line)]] | wt | 1.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.4× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 3.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.7× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 0.965 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 45.7× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 0.880 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +10.0) | — |
| [[J82 (line)]] | alt | 1.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.0× (z +9.6) | — |
| [[LoVo (line)]] | wt | 0.839 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +8.7) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 1.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 1.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.3× (z +9.5) | — |
| [[A-427 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.821 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.966 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.887 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.993 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.911 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUX2]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[RTN4RL1]] | +0.66 | +0.57 / +0.70 | both halves | 9e-06 | **novel candidate** |
| [[EFHD1]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SORCS3]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[TMEM266]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RIPOR2]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[PTPRO]] | +0.62 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[TMEFF2]] | +0.62 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MEIOC]] | +0.61 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[COL25A1]] | +0.61 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNB1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.0% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TLR2]] | B | TLR2 activity lowers KCNB1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without TLR2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[ELMO1]] | B | ELMO1 activity raises KCNB1's level | lines that do not express ELMO1 (17) vs lines expressing it (33) | 1.51× lower at baseline in the lines without ELMO1 | 0.095 | ⚠ within organs, on part of the lines; also absent: VEGFD, FRG1FP, NOVA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.0, 20.4); signed map (27.4, 20.2). **Vector** length 58.1, 9.21% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +31.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +14.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.8 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +3.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +3.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,293,394-49,484,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv2.1 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 6 pathways, smallest: Voltage gated Potassium channels; Glucagon-like Peptide-1 (GLP1) regulates insulin secretion; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14721](https://www.uniprot.org/uniprotkb/Q14721) (Potassium voltage-gated channel subfamily B member 1):

> Voltage-gated potassium channel that mediates transmembrane potassium transport in excitable membranes, primarily in the brain, but also in the pancreas and cardiovascular system. Contributes to the regulation of the action potential (AP) repolarization, duration and frequency of repetitive AP firing in neurons, muscle cells and endocrine cells and plays a role in homeostatic attenuation of electrical excitability throughout the brain. Plays also a role in the regulation of exocytosis …

**Summary**, from NCBI Gene [3745](https://www.ncbi.nlm.nih.gov/gene/3745):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. Four sequence-related potassium channel genes - shaker, shaw, shab, and shal - have been identified in Drosophila, and each has been shown to have …

**Accessions** — [HGNC:6231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6231) · Entrez [3745](https://www.ncbi.nlm.nih.gov/gene/3745) · UniProt [Q14721](https://www.uniprot.org/uniprotkb/Q14721) · Ensembl [ENSG00000158445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158445)

## Data

Gene col 8162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8162); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8162]; `tensor/DDL_lfc|DDL_z.npy` [8162]; `embed/gene_vectors.npy` [8162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8162 or target_col == 8162). Every well: [[KCNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
