---
symbol: "MKRN2"
type: "gene"
col: 1139
ensembl_id: "ENSG00000075975"
name: "makorin ring finger protein 2"
location: "3p25.2"
module: 30
arm: "+"
pooled_cpm: 27.36
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MKRN2

*makorin ring finger protein 2* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.91× (z +11.1, q 9e-26, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.477× (z -12.7, q 3e-34, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.753× (z -6.9, q 7e-10, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD9]] (+0.71, fdr 7e-06), [[UNC45A]] (+0.71, fdr 7e-06), [[RNF216P1]] (+0.71, fdr 2e-05); moves opposite to [[HIVEP1]] (-0.67, fdr 1e-05), [[ERCC6L2]] (-0.66, fdr 3e-05), [[HIVEP2-DT]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AXL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +11.1 | 9e-26 | 40/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +11.0 | 2e-25 | 41/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +9.6 | 2e-19 | 41/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +9.4 | 5e-19 | 40/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +9.0 | 2e-17 | 38/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +7.9 | 2e-13 | 33/48 (LS 180, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.7 | 2e-12 | 2/48 (A498, CFPAC-1) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +6.0 | 1e-07 | 25/48 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 22/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.8 | 0.007 | 18/48 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.031 | 12/40 (C32, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +3.3 | 0.053 | 12/48 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.477×** | -12.7 | 3e-34 | 35/43 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -11.6 | 7e-29 | 30/35 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.590×** | -8.4 | 9e-15 | 25/39 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -6.9 | 7e-10 | 26/48 (SNU-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -6.0 | 2e-07 | 27/48 (HOP62, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.848× | -4.0 | 0.005 | 23/47 (NCI-H1792, H4, …) | top dose only | composition shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.034 | 9/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.828× | -3.1 | 0.12 | 16/47 (HS-578T, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 43.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.97× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0573× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0816× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -10.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0622× (z -11.4) |
| [[HOP62 (line)]] | alt | 37.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.524× (z -8.5) |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -15.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0625× (z -16.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.9) |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD9]] | +0.71 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.71 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.71 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[NDUFA12]] | +0.71 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.71 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RTCA]] | +0.69 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[NBPF3]] | +0.69 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.69 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[DPY30]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.68 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[USP35]] | +0.67 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[NFRKB]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP1]] | -0.67 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.66 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[HIVEP2-DT]] | -0.66 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CDKN2B-AS1]] | -0.65 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[OSTM1]] | -0.65 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PSMD6-AS1]] | -0.65 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.65 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ZFP91]] | -0.64 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RFX3]] | -0.62 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | -0.62 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[TUG1]] | -0.62 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CLOCK]] | -0.61 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AXL]] | B | AXL activity raises MKRN2's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.17× lower at baseline in the lines without AXL | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.1, -5.1); signed map (-35.1, -4.2). **Vector** length 100, 23.5% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +5.1 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.6 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Brimonidine (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | makorin ring finger protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,557,057-12,586,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF62, HSPC070 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H000](https://www.uniprot.org/uniprotkb/Q9H000) (E3 ubiquitin-protein ligase makorin-2):

> E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto substrate proteins (By similarity). Promotes the polyubiquitination and proteasome-dependent degradation of RELA/p65, thereby suppressing RELA-mediated NF-kappaB transactivation and negatively regulating inflammatory responses (By similarity). Plays a role in the regulation of spermiation and in male fertility (By similarity).

**Summary**, from NCBI Gene [23609](https://www.ncbi.nlm.nih.gov/gene/23609):

> This gene encodes a probable E3 ubiquitin ligase containing several zinc finger domains, that is a member of the makorin RING zinc-finger protein family. This gene overlaps the v-raf-1 murine leukemia viral oncogene homolog 1 (RAF1) gene in an antisense orientation and may have a co-regulatory function with RAF1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:7113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7113) · Entrez [23609](https://www.ncbi.nlm.nih.gov/gene/23609) · UniProt [Q9H000](https://www.uniprot.org/uniprotkb/Q9H000) · Ensembl [ENSG00000075975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075975)

## Data

Gene col 1139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1139); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1139]; `tensor/DDL_lfc|DDL_z.npy` [1139]; `embed/gene_vectors.npy` [1139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1139 or target_col == 1139). Every well: [[MKRN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKRN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
