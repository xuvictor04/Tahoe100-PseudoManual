---
symbol: "PSMG1"
type: "gene"
col: 11415
ensembl_id: "ENSG00000183527"
name: "proteasome assembly chaperone 1"
location: "21q22.2"
module: 1
arm: "+"
pooled_cpm: 11.27
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PSMG1

*proteasome assembly chaperone 1* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +11.8, q 3e-29, up in 26 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.55× (z +7.1, q 8e-11, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.660× (z -6.8, q 8e-09, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFRD2]] (+0.77, fdr 7e-06), [[ATIC]] (+0.72, fdr 7e-06), [[HGH1]] (+0.70, fdr 7e-06); moves opposite to [[SERF2]] (-0.74, fdr 7e-06), [[ATP5F1E]] (-0.73, fdr 9e-06), [[MRPL33]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[S100A6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.07×** | +11.8 | 3e-29 | 26/38 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.08×** | +11.4 | 1e-27 | 18/19 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +8.8 | 2e-16 | 35/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.68×** | +8.4 | 8e-15 | 33/47 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.74×** | +8.3 | 2e-14 | 20/26 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.1 | 8e-11 | 25/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +7.1 | 1e-10 | 22/46 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.53×** | +6.9 | 3e-10 | 30/47 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.1 | 7e-08 | 19/40 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.43×** | +5.7 | 5e-07 | 19/47 (A549, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 4e-05 | 16/45 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.9 | 4e-05 | 16/39 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +4.7 | 1e-04 | 13/44 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.4 | 3e-04 | 12/46 (PANC-1, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.4 | 5e-04 | 19/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +4.2 | 9e-04 | 8/44 (CFPAC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.001 | 7/44 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 14/46 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 10/47 (NCI-H460, SNU-423, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.018 | 2/44 (Hs 766T, SNU-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.030 | 9/44 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.073 | 5/43 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 1.14× | +2.9 | 0.075 | 0/48 | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +2.8 | 0.091 | 5/42 (CFPAC-1, BT-474, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.660×** | -6.8 | 8e-09 | 25/46 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rifaximin (drug)]] 5 µM |  | **0.776×** | -4.0 | 0.013 | 9/46 (RPMI-7951, RKO, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.784×** | -4.0 | 0.013 | 12/47 (LOX-IMVI, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (dihydrochloride) (drug)]] 0.05 µM |  | **0.782×** | -3.7 | 0.029 | 11/46 (C-33 A, A549, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.089 | 7/43 (RPMI-7951, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.099 | 12/46 (A-427, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0912× (z -9.1) ⚠ toxic |
| [[A498 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.271× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 7.89 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.168× (z -8.6) |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0613× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0838× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 8.64 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.139× (z -9.2) |
| [[RKO (line)]] | wt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.9) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.122× (z -8.7) |
| [[SW480 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFRD2]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[ATIC]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[HGH1]] | +0.70 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[BOP1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[PRPS1]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[BCS1L]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 | STRING 510 |
| [[RUVBL1]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 | STRING 625 |
| [[POGK]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[FARSB]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[WDR77]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERF2]] | -0.74 | -0.64 / -0.74 | both halves | 7e-06 |  |
| [[ATP5F1E]] | -0.73 | -0.57 / -0.76 | both halves | 9e-06 |  |
| [[MRPL33]] | -0.70 | -0.49 / -0.70 | both halves | 1e-05 | STRING 822 |
| [[UQCRB]] ⚠ | -0.69 | -0.61 / -0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA1]] | -0.67 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.66 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[APTR]] | -0.66 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[COX17]] | -0.66 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[NDUFA4]] | -0.66 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[RPS19]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[UBL5]] | -0.65 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[CLDN18]] | -0.65 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[OST4]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A6]] | B | S100A6 activity lowers PSMG1's level | lines that do not express S100A6 (5) vs lines expressing it (45) | 1.53× higher at baseline in the lines without S100A6 | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRC5D-AS1, HLA-H, PRRG1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.7, -36.0); signed map (-6.4, -45.3). **Vector** length 65.4, 10.3% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.0 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.8 | +8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +1.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | proteasome assembly chaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,174,769-39,183,488 (-) |
| Ensembl biotype | protein_coding |
| Also known as | c21-LRP, LRPC21, PAC1; previously DSCR2 |
| Hallmark sets | SPERMATOGENESIS, MTORC1_SIGNALING |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [O95456](https://www.uniprot.org/uniprotkb/O95456) (Proteasome assembly chaperone 1):

> Chaperone protein which promotes assembly of the 20S proteasome as part of a heterodimer with PSMG2. The PSMG1-PSMG2 heterodimer binds to the PSMA5 and PSMA7 proteasome subunits, promotes assembly of the proteasome alpha subunits into the heteroheptameric alpha ring and prevents alpha ring dimerization.

**Summary**, from NCBI Gene [8624](https://www.ncbi.nlm.nih.gov/gene/8624):

> Enables molecular adaptor activity. Involved in chaperone-mediated protein complex assembly and proteasome core complex assembly. Located in several cellular components, including Golgi apparatus; endoplasmic reticulum; and nucleoplasm. Part of protein folding chaperone complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3043) · Entrez [8624](https://www.ncbi.nlm.nih.gov/gene/8624) · UniProt [O95456](https://www.uniprot.org/uniprotkb/O95456) · Ensembl [ENSG00000183527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183527)

## Data

Gene col 11415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11415); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11415]; `tensor/DDL_lfc|DDL_z.npy` [11415]; `embed/gene_vectors.npy` [11415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11415 or target_col == 11415). Every well: [[PSMG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
