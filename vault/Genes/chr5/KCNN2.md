---
symbol: "KCNN2"
type: "gene"
col: 1288
ensembl_id: "ENSG00000080709"
name: "potassium calcium-activated channel subfamily N member 2"
location: "5q22.3"
module: 61
arm: "+"
pooled_cpm: 4.61
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# KCNN2

*potassium calcium-activated channel subfamily N member 2* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.69× (z +29.7, q 0e+00, up in 21 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 5 µM in 1 line (SW48 0.0531×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.108×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC80]] (+0.64, fdr 7e-06), [[ADAMTSL1]] (+0.64, fdr 1e-05), [[LDB2]] (+0.61, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GABRG3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.69×** | +29.7 | 0e+00 | 21/24 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.35×** | +23.0 | 0e+00 | 21/24 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.37×** | +20.5 | 0e+00 | 29/30 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.55×** | +19.0 | 0e+00 | 27/28 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.82×** | +16.2 | 0e+00 | 28/29 (C32, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.99×** | +15.3 | 0e+00 | 28/29 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.82×** | +14.8 | 0e+00 | 16/22 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.79×** | +14.2 | 1e-43 | 22/28 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.14×** | +12.6 | 7e-35 | 27/30 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +12.6 | 2e-34 | 3/10 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +10.3 | 5e-23 | 2/5 (SK-MEL-2, HT-29) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +10.1 | 4e-22 | 0/4 | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +9.3 | 4e-19 | 13/26 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.07×** | +8.0 | 4e-14 | 20/27 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +7.3 | 8e-12 | 11/29 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +6.6 | 2e-09 | 7/29 (SK-MEL-2, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.8 | 2e-07 | 2/22 (NCI-H460, HEC-1-A) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.67×** | +5.7 | 5e-07 | 15/27 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1288.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 5 µM in 1 line (SW48 0.0531×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.108×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.825× | -3.0 | 0.97 | 1/32 (CFPAC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.43 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.16× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 5.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +18.0) | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.62× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 19.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +12.6) | [[Sunitinib (drug)]] 5 µM 0.0531× (z -12.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 1.30 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 1.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +10.2) | — |
| [[C32 (line)]] | wt | 3.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.64× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +8.8) | — |
| [[J82 (line)]] | alt | 1.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +10.7) | — |
| [[A-172 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.949 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC80]] | +0.64 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ADAMTSL1]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[LDB2]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[EPHB1]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PKNOX2]] | +0.60 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.60 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[XKR4]] | +0.59 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SLC14A2]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CACNA1A]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 | pathway: Neuronal System |
| [[KCNIP1]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.59 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[MTUS2]] | +0.59 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR4527HG]] | B | MIR4527HG activity raises KCNN2's level | lines that do not express MIR4527HG (36) vs lines expressing it (14) | 2.11× lower at baseline in the lines without MIR4527HG | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADGRG7, UNC5D, ENSG00000287474 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRG3]] | B | KCNN2 activity raises GABRG3's level | lines that do not express KCNN2 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without KCNN2 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 33.5); signed map (33.0, 26.9). **Vector** length 44.8, 6.78% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +29.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily N member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:114,055,926-114,496,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KCa2.2, hSK2 |
| Gene groups (HGNC) | Potassium calcium-activated channels |
| Reactome | 7 pathways, smallest: Acetylcholine inhibits contraction of outer hair cells; Ca2+ activated K+ channels; Sensory processing of sound by outer hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2S1](https://www.uniprot.org/uniprotkb/Q9H2S1) (Small conductance calcium-activated potassium channel protein 2):

> Small conductance calcium-activated potassium channel that mediates the voltage-independent transmembrane transfer of potassium across the cell membrane through a constitutive interaction with calmodulin which binds the intracellular calcium allowing its opening. The current is characterized by a voltage-independent activation, an intracellular calcium concentration increase-dependent activation and a single-channel conductance of about 3 picosiemens. Also presents an inwardly rectifying …

**Summary**, from NCBI Gene [3781](https://www.ncbi.nlm.nih.gov/gene/3781):

> Action potentials in vertebrate neurons are followed by an afterhyperpolarization (AHP) that may persist for several seconds and may have profound consequences for the firing pattern of the neuron. Each component of the AHP is kinetically distinct and is mediated by different calcium-activated potassium channels. The protein encoded by this gene is activated before membrane hyperpolarization and is thought to regulate neuronal excitability by contributing to the slow component of synaptic AHP. …

**Accessions** — [HGNC:6291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6291) · Entrez [3781](https://www.ncbi.nlm.nih.gov/gene/3781) · UniProt [Q9H2S1](https://www.uniprot.org/uniprotkb/Q9H2S1) · Ensembl [ENSG00000080709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080709)

## Data

Gene col 1288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1288); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1288]; `tensor/DDL_lfc|DDL_z.npy` [1288]; `embed/gene_vectors.npy` [1288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1288 or target_col == 1288). Every well: [[KCNN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
