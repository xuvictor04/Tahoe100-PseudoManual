---
symbol: "WHAMMP3"
type: "gene"
col: 15867
ensembl_id: "ENSG00000276141"
name: "WHAMM pseudogene 3"
location: "15q11.2"
module: 46
arm: "+"
pooled_cpm: 6.94
n_lines_expressing: 44
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# WHAMMP3

*WHAMM pseudogene 3* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.42× (z +4.6, q 0.003, up in 3 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.54× (z +4.1, q 0.010, up in 7 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.306× (z -15.9, q 0e+00, down in 33 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WHAMMP2]] (+0.85, fdr 7e-06), [[ACBD5]] (+0.61, fdr 1e-05), [[RBM43]] (+0.60, fdr 4e-05); moves opposite to [[CMIP]] (-0.54, fdr 4e-05), [[MICAL2]] (-0.53, fdr 1e-04), [[VMP1]] (-0.51, fdr 9e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WHAMMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.6 | 0.003 | 3/19 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.010 | 7/36 (MIA PaCa-2, A498, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.27× | +3.2 | 0.22 | 9/30 (AsPC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.306×** | -15.9 | 0e+00 | 33/39 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.315×** | -15.5 | 0e+00 | 32/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.395×** | -12.5 | 2e-33 | 30/40 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.517×** | -8.9 | 1e-16 | 27/40 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -5.4 | 7e-06 | 13/30 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -5.3 | 1e-05 | 13/42 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.5 | 5e-04 | 14/41 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.741×** | -4.0 | 0.004 | 9/40 (C32, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -4.0 | 0.004 | 14/41 (A498, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.578×** | -3.9 | 0.007 | 6/39 (A498, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.762×** | -3.7 | 0.013 | 15/36 (Panc 03.27, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.767×** | -3.4 | 0.029 | 13/34 (SNU-1, CFPAC-1, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.1 | 0.074 | 4/39 (H4, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -11.3) |
| [[C32 (line)]] | wt | 12.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0907× (z -11.4) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.159× (z -10.1) |
| [[A498 (line)]] | wt | 6.05 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0632× (z -14.2) |
| [[A549 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0706× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0675× (z -11.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 7.22 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -10.6) |
| [[HS-578T (line)]] | alt | 4.97 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0524× (z -10.5) |
| [[J82 (line)]] | alt | 11.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -8.6) |
| [[LoVo (line)]] | wt | 3.82 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.233× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 6.07 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.120× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 8.91 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -8.8) |
| [[PANC-1 (line)]] | alt | 9.40 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -9.1) |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -8.5) |
| [[SW480 (line)]] | alt | 11.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -9.0) |
| [[A-427 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMMP2]] | +0.85 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ACBD5]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RBM43]] | +0.60 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RSRC2]] | +0.57 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[LINC02256]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DNAJC27]] | +0.55 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ZNF563]] | +0.54 | +0.38 / +0.32 | both halves | 2e-04 |  |
| [[SHOX2]] | +0.54 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[ZCCHC8]] | +0.53 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[TSR2]] | +0.53 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[PUS10]] | +0.52 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[NFYB]] | +0.52 | +0.37 / +0.39 | both halves | 9e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MICAL2]] | -0.53 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[VMP1]] | -0.51 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[TRAPPC9]] | -0.51 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[MPRIP]] | -0.50 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ITGA6]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ACTN4]] | -0.49 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[MTAP]] | -0.48 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CORO1C]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[MIR222HG]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MED14]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[GATAD2A]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHAMMP2]] | B | WHAMMP2 activity raises WHAMMP3's level | lines that do not express WHAMMP2 (10) vs lines expressing it (40) | 2.80× lower at baseline in the lines without WHAMMP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LIFR, ZNF512B, ENSG00000286964; maybe low, not absent; its own permutation p |
| [[MST1R]] | B | MST1R activity lowers WHAMMP3's level | lines that do not express MST1R (24) vs lines expressing it (26) | 1.81× higher at baseline in the lines without MST1R | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (5.1, -26.9); signed map (12.4, -13.4). **Vector** length 51.8, 7.48% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -15.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -12.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.9 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[vincristine (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -0.9 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -0.9 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | WHAMM pseudogene 3 |
| Locus type | pseudogene |
| Location | 15q11.2 — chr15:22,664,359-22,681,605 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously WHDC1L1, WHAMML1 |
| Matched by | ensembl_id |

UniProt [Q1A5X7](https://www.uniprot.org/uniprotkb/Q1A5X7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27892) · Entrez [339005](https://www.ncbi.nlm.nih.gov/gene/339005) · UniProt [Q1A5X7](https://www.uniprot.org/uniprotkb/Q1A5X7) · Ensembl [ENSG00000276141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276141)

## Data

Gene col 15867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15867); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15867]; `tensor/DDL_lfc|DDL_z.npy` [15867]; `embed/gene_vectors.npy` [15867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15867 or target_col == 15867). Every well: [[WHAMMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WHAMMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
