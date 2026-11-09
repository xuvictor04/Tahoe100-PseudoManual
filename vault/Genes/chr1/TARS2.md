---
symbol: "TARS2"
type: "gene"
col: 6727
ensembl_id: "ENSG00000143374"
name: "threonyl-tRNA synthetase 2, mitochondrial"
location: "1q21.2"
module: 12
arm: "+"
pooled_cpm: 25.37
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TARS2

*threonyl-tRNA synthetase 2, mitochondrial* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.31× (z +4.6, q 0.002, up in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.73× (z +4.3, q 0.004, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.564× (z -7.3, q 1e-10, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEO1]] (+0.77, fdr 7e-06), [[RP9]] (+0.73, fdr 7e-06), [[NEMF]] (+0.73, fdr 7e-06); moves opposite to [[UBE2V1]] (-0.67, fdr 1e-05), [[MOB1A]] (-0.65, fdr 1e-05), [[PGRMC1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FSTL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.31×** | +4.6 | 0.002 | 24/47 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.3 | 0.004 | 26/46 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.020 | 19/47 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.041 | 23/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.041 | 19/48 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.064 | 18/48 (LS 180, CHP-212, …) | top dose only |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | 1.47× | +3.0 | 0.20 | 9/48 (LS 180, SNU-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -7.3 | 1e-10 | 39/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -7.2 | 2e-10 | 36/48 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.592×** | -6.7 | 4e-09 | 35/47 (A-427, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.584×** | -6.6 | 5e-09 | 20/33 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -6.4 | 2e-08 | 36/46 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -6.3 | 3e-08 | 27/43 (SW 900, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -5.7 | 7e-07 | 22/39 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -5.2 | 1e-05 | 28/46 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -4.6 | 3e-04 | 27/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.010 | 25/48 (SW480, SW 1271, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.3 | 0.048 | 20/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -3.3 | 0.048 | 22/48 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.057 | 19/48 (HOP62, A498, …) | top dose only |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.077 | 13/48 (SNU-1, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 26.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -14.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -8.6) |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.201× (z -8.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.293× (z -9.7) |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.4) ⚠ cell-cycle shift, explains ~57% of this change | [[AZD2858 (drug)]] 0.5 µM 0.108× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.322× (z -8.6) |
| [[SW48 (line)]] | wt | 20.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0919× (z -9.8) |
| [[A-172 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEO1]] | +0.77 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[RP9]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[NEMF]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[MTRES1]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TMEM216]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.70 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[PET117]] | +0.69 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[GEMIN2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.67 | +0.47 / +0.72 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RIOK2]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RPUSD2]] | +0.67 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[MRPL46]] | +0.67 | +0.49 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2V1]] | -0.67 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[APP]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.62 | -0.32 / -0.67 | both halves | 1e-04 |  |
| [[PDIA3P1]] | -0.60 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[STMP1]] | -0.60 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[FUCA2]] | -0.59 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CERS2]] | -0.59 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[EEF1A1]] | -0.58 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[LAMC1]] | -0.58 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[DHFR]] | -0.58 | -0.32 / -0.62 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL1]] | B | FSTL1 activity lowers TARS2's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without FSTL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[TOP2A]] | B | TOP2A activity raises TARS2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.8, -8.6); signed map (-15.9, -9.5). **Vector** length 105, 28.3% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.8 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.8 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | threonyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,487,414-150,507,602 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12528; previously TARSL1 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW92](https://www.uniprot.org/uniprotkb/Q9BW92) (Threonine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr). Also edits incorrectly charged tRNA(Thr) via its editing domain.

**Summary**, from NCBI Gene [80222](https://www.ncbi.nlm.nih.gov/gene/80222):

> This gene encodes a member of the class-II aminoacyl-tRNA synthetase family. The encoded protein is a mitochondrial aminoacyl-tRNA synthetase. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 4. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:30740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30740) · Entrez [80222](https://www.ncbi.nlm.nih.gov/gene/80222) · UniProt [Q9BW92](https://www.uniprot.org/uniprotkb/Q9BW92) · Ensembl [ENSG00000143374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143374)

## Data

Gene col 6727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6727); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6727]; `tensor/DDL_lfc|DDL_z.npy` [6727]; `embed/gene_vectors.npy` [6727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6727 or target_col == 6727). Every well: [[TARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
