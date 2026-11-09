---
symbol: "KANK3"
type: "gene"
col: 11875
ensembl_id: "ENSG00000186994"
name: "KN motif and ankyrin repeat domains 3"
location: "19p13.2"
module: 100
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# KANK3

*KN motif and ankyrin repeat domains 3* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.63× (z +14.7, q 0e+00, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.547× (z -5.8, q 4e-06, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HES2]] (+0.71, fdr 7e-06), [[TMEM266]] (+0.65, fdr 1e-05), [[CELF5]] (+0.65, fdr 1e-05); moves opposite to [[TTF2]] (-0.47, fdr 1e-04), [[NNT]] (-0.47, fdr 4e-04), [[PPWD1]] (-0.46, fdr 8e-04, ⚠ one half only (not replicated)), [[QSER1]] (-0.46, fdr 2e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRDM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.63×** | +14.7 | 0e+00 | 31/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.89×** | +14.4 | 1e-44 | 31/42 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.06×** | +13.4 | 6e-39 | 33/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +11.1 | 3e-26 | 19/30 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.81×** | +9.9 | 5e-21 | 27/36 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.2 | 4e-18 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +8.8 | 1e-16 | 27/43 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +5.8 | 6e-07 | 20/44 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +4.8 | 1e-04 | 1/2 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.7 | 2e-04 | 1/12 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +4.5 | 3e-04 | 8/43 (LoVo, A498, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.011 | 6/20 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.011 | 6/37 (NCI-H2347, NCI-H1573, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.068 | 6/41 (NCI-H460, NCI-H2030, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -5.8 | 4e-06 | 20/45 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.548×** | -5.6 | 8e-06 | 17/40 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -5.3 | 2e-05 | 19/43 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -5.1 | 6e-05 | 19/40 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.618×** | -4.6 | 4e-04 | 12/44 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -4.5 | 8e-04 | 15/43 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -3.4 | 0.063 | 11/35 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.723× | -3.1 | 0.13 | 17/40 (NCI-H1573, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.726× | -3.1 | 0.13 | 9/37 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 3.76 | 0 | 1 | — | [[Diphenhydramine (drug)]] 5 µM 0.0649× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.35 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[A-172 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.981 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.735 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES2]] | +0.71 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[TMEM266]] | +0.65 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[CELF5]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[RASGEF1A]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[LGI4]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[KLC3]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[CAMK2B]] | +0.58 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[CDH23]] | +0.57 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[SPTBN4]] | +0.56 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[MYO1F]] | +0.56 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[RYR1]] | +0.55 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PPM1N]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTF2]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[NNT]] | -0.47 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[PPWD1]] | -0.46 | -0.19 / -0.54 | ⚠ one half (not replicated) | 8e-04 |  |
| [[QSER1]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[QRSL1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM1]] | B | PRDM1 activity lowers KANK3's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 1.34× higher at baseline in the lines without PRDM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1 |
| [[CCDC33]] | B | CCDC33 activity lowers KANK3's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.22× higher at baseline in the lines without CCDC33 | 0.058 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[NRTN]] | C | NRTN activity raises KANK3's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without NRTN | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.5, 34.7); signed map (27.0, 20.3). **Vector** length 52.0, 6.98% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.6 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | KN motif and ankyrin repeat domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,322,584-8,343,262 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46061; previously ANKRD47 |
| Gene groups (HGNC) | KN motif and ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NY19](https://www.uniprot.org/uniprotkb/Q6NY19) (KN motif and ankyrin repeat domain-containing protein 3):

> May be involved in the control of cytoskeleton formation by regulating actin polymerization.

**Summary**, from NCBI Gene [256949](https://www.ncbi.nlm.nih.gov/gene/256949):

> Predicted to be involved in negative regulation of actin filament polymerization. Predicted to be active in cytoplasm and cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24796) · Entrez [256949](https://www.ncbi.nlm.nih.gov/gene/256949) · UniProt [Q6NY19](https://www.uniprot.org/uniprotkb/Q6NY19) · Ensembl [ENSG00000186994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186994)

## Data

Gene col 11875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11875); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11875]; `tensor/DDL_lfc|DDL_z.npy` [11875]; `embed/gene_vectors.npy` [11875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11875 or target_col == 11875). Every well: [[KANK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
