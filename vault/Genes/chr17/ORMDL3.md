---
symbol: "ORMDL3"
type: "gene"
col: 10205
ensembl_id: "ENSG00000172057"
name: "ORMDL sphingolipid biosynthesis regulator 3"
location: "17q21.1"
module: 40
arm: "+"
pooled_cpm: 22.01
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ORMDL3

*ORMDL sphingolipid biosynthesis regulator 3* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.08× (z +12.9, q 4e-35, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.602× (z -12.6, q 9e-34, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSDMB]] (+0.76, fdr 7e-06, ⚠ same locus), [[YIPF2]] (+0.71, fdr 7e-06), [[GGCX]] (+0.69, fdr 7e-06), [[SGSM3]] (+0.65, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.65, fdr 1e-05), [[ST7L]] (-0.63, fdr 3e-05), [[ANGPT2]] (-0.61, fdr 5e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +12.9 | 4e-35 | 38/48 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +12.4 | 4e-33 | 40/48 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +10.8 | 9e-25 | 40/47 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +6.0 | 3e-07 | 22/45 (KATO III, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.0 | 5e-05 | 16/48 (BT-474, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.9 | 1e-04 | 16/35 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 2e-04 | 18/48 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.5 | 5e-04 | 18/41 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 16/47 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.1 | 0.002 | 13/31 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -12.6 | 9e-34 | 32/47 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -10.3 | 3e-22 | 32/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.558×** | -9.5 | 4e-19 | 30/46 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.407×** | -8.2 | 2e-14 | 33/48 (SW 900, A498, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -6.0 | 3e-07 | 21/47 (AsPC-1, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.737×** | -5.4 | 7e-06 | 23/48 (AsPC-1, H4, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -5.3 | 7e-06 | 21/47 (AsPC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -5.1 | 2e-05 | 20/45 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.766×** | -4.7 | 2e-04 | 13/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.777×** | -4.2 | 0.002 | 18/47 (LoVo, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.9 | 0.006 | 3/48 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.802×** | -3.6 | 0.016 | 7/48 (H4, A-427, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.016 | 12/46 (HOP62, AN3 CA, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.817×** | -3.5 | 0.016 | 17/47 (AsPC-1, SW 900, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.016 | 15/47 (HepG2/C3A, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.720×** | -3.0 | 0.081 | 7/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 28.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.8) |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0597× (z -17.7) |
| [[BT-474 (line)]] | alt | 142 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.183× (z -10.5) |
| [[LoVo (line)]] | wt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.9) |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0755× (z -10.6) |
| [[A498 (line)]] | wt | 60.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 19.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +8.8) | — |
| [[KATO III (line)]] | alt | 33.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.363× (z -11.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.2) |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.110× (z -8.5) |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -18.4) |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSDMB]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 | STRING 971; ⚠ same locus (1.2 kb, same strand: neighbours can correlate without regulation) |
| [[YIPF2]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[GGCX]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SGSM3]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CYB561D2]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[C2CD2L]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DOK4]] | +0.64 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ADIPOR1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NPRL2]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GPR107]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TCIRG1]] | +0.63 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.65 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ST7L]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ANGPT2]] | -0.61 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[WARS2-AS1]] | -0.61 | -0.58 / -0.32 | both halves | 1e-04 |  |
| [[ZNF518A]] | -0.59 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[METTL18]] | -0.58 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.58 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[TCF12]] | -0.58 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[NNT-AS1]] | -0.57 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[GTF2H1]] | -0.57 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[MED1]] | -0.57 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ORMDL3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.5, -31.3); signed map (-48.1, 8.6). **Vector** length 97.7, 21.0% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +12.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +1.7 | +0.0 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | +1.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ORMDL sphingolipid biosynthesis regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:39,921,041-39,927,601 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ORMDL sphingolipid biosynthesis regulators |
| Reactome | 5 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N138](https://www.uniprot.org/uniprotkb/Q8N138) (ORM1-like protein 3):

> Plays an essential role in the homeostatic regulation of sphingolipid de novo biosynthesis by modulating the activity of the serine palmitoyltransferase (SPT) in response to ceramide levels. When complexed to SPT, the binding of ceramides to its N-terminus stabilizes a conformation that block SPT substrate entry, hence preventing SPT catalytic activity. Through this mechanism, maintains ceramide levels at sufficient concentrations for the production of complex sphingolipids, but which prevents …

**Summary**, from NCBI Gene [94103](https://www.ncbi.nlm.nih.gov/gene/94103):

> Involved in ceramide metabolic process. Acts upstream of or within several processes, including negative regulation of B cell apoptotic process; negative regulation of ceramide biosynthetic process; and positive regulation of protein localization to nucleus. Located in endoplasmic reticulum. Part of serine palmitoyltransferase complex. Implicated in allergic asthma; asthma; and childhood-onset asthma. Biomarker of allergic asthma and asthma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16038) · Entrez [94103](https://www.ncbi.nlm.nih.gov/gene/94103) · UniProt [Q8N138](https://www.uniprot.org/uniprotkb/Q8N138) · Ensembl [ENSG00000172057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172057)

## Data

Gene col 10205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10205); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10205]; `tensor/DDL_lfc|DDL_z.npy` [10205]; `embed/gene_vectors.npy` [10205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10205 or target_col == 10205). Every well: [[ORMDL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORMDL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
