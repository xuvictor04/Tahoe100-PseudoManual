---
symbol: "ELAVL3"
type: "gene"
col: 12185
ensembl_id: "ENSG00000196361"
name: "ELAV like RNA binding protein 3"
location: "19p13.2"
module: 53
arm: "+"
pooled_cpm: 4.45
n_lines_expressing: 48
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# ELAVL3

*ELAV like RNA binding protein 3* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.37× (z +20.6, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Fusidic acid (drug)]] 5 µM: 0.763× (z -3.8, q 0.078, down in 12 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HEC-1-A 0.109×; ⚠ toxic; cell-cycle shift, explains ~61% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE9]] (+0.79, fdr 7e-06), [[TMPRSS9]] (+0.79, fdr 7e-06), [[CPT1C]] (+0.78, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SH2D4B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.37×** | +20.6 | 0e+00 | 30/34 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +15.5 | 0e+00 | 24/35 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.15×** | +13.5 | 3e-39 | 2/3 (SHP-77, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +10.5 | 2e-23 | 12/16 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +9.7 | 3e-20 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +6.9 | 4e-10 | 20/41 (SK-MEL-2, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +6.7 | 2e-09 | 15/33 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +6.4 | 2e-08 | 18/43 (C-33 A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +6.2 | 3e-08 | 20/42 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +5.9 | 2e-07 | 18/44 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +5.3 | 8e-06 | 15/40 (SK-MEL-2, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.0 | 3e-05 | 2/15 (SHP-77, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.7 | 1e-04 | 16/45 (SK-MEL-2, SNU-423, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.5 | 3e-04 | 7/45 (PANC-1, A-172, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **2.05×** | +3.7 | 0.008 | 1/20 (A498) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.008 | 4/34 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.010 | 15/44 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.011 | 6/25 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.024 | 8/42 (HT-29, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12185.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HEC-1-A 0.109×; ⚠ toxic; cell-cycle shift, explains ~61% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fusidic acid (drug)]] 5 µM |  | **0.763×** | -3.8 | 0.078 | 12/45 (C-33 A, NCI-H661, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.739× | -3.0 | 0.34 | 7/43 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 0.05 µM |  | 0.740× | -3.0 | 0.34 | 3/45 (HS-578T, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 11.9 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.78× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 29.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.85× (z +10.5) | — |
| [[A549 (line)]] | wt | 2.29 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 29.8× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 2.10 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 44.3× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 5.66 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[HOP62 (line)]] | alt | 1.92 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 29.3× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 90.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.68× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +10.9) | — |
| [[C32 (line)]] | wt | 2.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.4× (z +8.7) | — |
| [[LoVo (line)]] | wt | 2.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE9]] | +0.79 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[MASP2]] | +0.77 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[CCNP]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.75 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[KIF17]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[EFNA2]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SLC8A2]] | +0.72 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH2D4B]] | C | SH2D4B activity lowers ELAVL3's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.76× higher at baseline in the lines without SH2D4B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.836). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.5, -15.8); signed map (20.5, 12.7). **Vector** length 60.9, 8.37% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +20.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ELAV like RNA binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,451,326-11,481,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUC, PLE21, DKFZp547J036, HUCL, MGC20653 |
| Gene groups (HGNC) | RNA binding motif containing; ELAV like RNA binding protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14576](https://www.uniprot.org/uniprotkb/Q14576) (ELAV-like protein 3):

> RNA-binding protein that binds to AU-rich element (ARE) sequences of target mRNAs, including VEGF mRNA. May also bind poly-A tracts via RRM 3 (By similarity). May be involved in neuronal differentiation and maintenance (By similarity). Plays a role in the stabilization of GAP43 mRNA and in spatial learning (By similarity).

**Summary**, from NCBI Gene [1995](https://www.ncbi.nlm.nih.gov/gene/1995):

> A member of the ELAVL protein family, ELAV-like 3 is a neural-specific RNA-binding protein which contains three RNP-type RNA recognition motifs. The observation that ELAVL3 is one of several Hu antigens (neuronal-specific RNA-binding proteins) recognized by the anti-Hu serum antibody present in sera from patients with paraneoplastic encephalomyelitis and sensory neuronopathy (PEM/PSN) suggests it has a role in neurogenesis. Two alternatively spliced transcript variants encoding distinct …

**Accessions** — [HGNC:3314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3314) · Entrez [1995](https://www.ncbi.nlm.nih.gov/gene/1995) · UniProt [Q14576](https://www.uniprot.org/uniprotkb/Q14576) · Ensembl [ENSG00000196361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196361)

## Data

Gene col 12185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12185); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12185]; `tensor/DDL_lfc|DDL_z.npy` [12185]; `embed/gene_vectors.npy` [12185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12185 or target_col == 12185). Every well: [[ELAVL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELAVL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
