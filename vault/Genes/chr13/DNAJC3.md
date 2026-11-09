---
symbol: "DNAJC3"
type: "gene"
col: 2258
ensembl_id: "ENSG00000102580"
name: "DnaJ heat shock protein family (Hsp40) member C3"
location: "13q32.1"
module: 42
arm: "+"
pooled_cpm: 202.66
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# DNAJC3

*DnaJ heat shock protein family (Hsp40) member C3* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +8.2, q 1e-13, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.567× (z -8.1, q 3e-13, down in 41 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.678× (z -5.8, q 2e-06, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA5]] (+0.78, fdr 7e-06), [[COPA]] (+0.77, fdr 7e-06), [[SEL1L]] (+0.77, fdr 7e-06); moves opposite to [[TRMT5]] (-0.56, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +8.2 | 1e-13 | 45/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +6.9 | 2e-09 | 35/48 (C32, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.6 | 7e-09 | 35/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.4 | 2e-08 | 35/47 (LOX-IMVI, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +6.2 | 5e-08 | 39/47 (C32, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.6 | 2e-06 | 31/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.4 | 4e-06 | 30/46 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.3 | 8e-06 | 34/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 1e-04 | 36/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.7 | 2e-04 | 29/47 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +4.3 | 7e-04 | 25/47 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 9e-04 | 30/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +4.2 | 0.001 | 27/47 (NCI-H2347, LOX-IMVI, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.0 | 0.003 | 29/44 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.011 | 26/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.017 | 25/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.068 | 22/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.080 | 21/47 (HT-29, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -8.1 | 3e-13 | 41/46 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.678×** | -5.8 | 2e-06 | 41/47 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.745×** | -4.2 | 0.005 | 32/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -4.1 | 0.007 | 28/47 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.760×** | -3.8 | 0.019 | 28/46 (LoVo, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.784×** | -3.5 | 0.046 | 29/48 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.786×** | -3.4 | 0.046 | 23/47 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.795×** | -3.4 | 0.046 | 30/47 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.068 | 24/48 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.808× | -3.1 | 0.12 | 21/47 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.816× | -3.0 | 0.13 | 21/47 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 104 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 114 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.1) | — |
| [[C32 (line)]] | wt | 149 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 29.5× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 546 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -12.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 536 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -11.1) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 140 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 136 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.37× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 230 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~58% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -9.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 296 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +8.8) ⚠ toxic | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.498× (z -8.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 168 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.53× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 188 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.498× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 170 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.7) | — |
| [[J82 (line)]] | alt | 300 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.3) | — |
| [[KATO III (line)]] | alt | 429 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.327× (z -12.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -9.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.480× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.359× (z -9.9) ⚠ toxic |
| [[SW48 (line)]] | wt | 170 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.07× (z +11.3) | — |
| [[A-427 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 237 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 660 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 224 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 179 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 264 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 223 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 245 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA5]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 978 |
| [[COPA]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SEL1L]] | +0.77 | +0.77 / +0.76 | both halves | 7e-06 | STRING 611 |
| [[HSP90B1]] | +0.76 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 927 |
| [[SEC24D]] | +0.75 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[HYOU1]] | +0.75 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 928 |
| [[MANF]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | STRING 613 |
| [[PDIA4]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 | STRING 812 |
| [[SEC61A1]] | +0.75 | +0.82 / +0.68 | both halves | 7e-06 | STRING 762 |
| [[TXNDC11]] | +0.75 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[NUCB2]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 | STRING 411 |
| [[PDIA6]] | +0.72 | +0.73 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 944 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | -0.56 | -0.54 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises DNAJC3's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without AGR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[GALNT3]] | B | GALNT3 activity raises DNAJC3's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.69× lower at baseline in the lines without GALNT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[CADPS2]] | B | CADPS2 activity raises DNAJC3's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without CADPS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[DNAJB9]] | C | DNAJB9's natural level weakens DNAJC3's drug response | DNAJB9's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.43; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -31.2); signed map (-54.3, 8.0). **Vector** length 134, 50.7% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.50 to 23); *Cargo concentration in the ER* (reactome, mean cos +0.55 to 7); *N-glycan trimming in the ER and Calnexin/Calreticulin cycle* (reactome, mean cos +0.58 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.6 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.6 | -5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.9 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -0.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:95,677,139-95,794,988 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P58, P58IPK, HP58, ERdj6, p58(IPK); previously PRKRI |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; Tetratricopeptide repeat domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, APOPTOSIS |
| Reactome | 20 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Maturation of DENV proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13217](https://www.uniprot.org/uniprotkb/Q13217) (DnaJ homolog subfamily C member 3):

> Involved in the unfolded protein response (UPR) during endoplasmic reticulum (ER) stress. Acts as a negative regulator of the EIF2AK4/GCN2 kinase activity by preventing the phosphorylation of eIF-2-alpha at 'Ser-52' and hence attenuating general protein synthesis under ER stress, hypothermic and amino acid starving stress conditions (By similarity). Co-chaperone of HSPA8/HSC70, it stimulates its ATPase activity. May inhibit both the autophosphorylation of EIF2AK2/PKR and the ability of EIF2AK2 …

**Summary**, from NCBI Gene [5611](https://www.ncbi.nlm.nih.gov/gene/5611):

> This gene encodes a protein with multiple tetratricopeptide repeat (TPR) motifs as well as the highly conserved J domain found in DNAJ chaperone family members. It is a member of the tetratricopeptide repeat family of proteins and acts as an inhibitor of the interferon-induced, dsRNA-activated protein kinase (PKR). [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:9439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9439) · Entrez [5611](https://www.ncbi.nlm.nih.gov/gene/5611) · UniProt [Q13217](https://www.uniprot.org/uniprotkb/Q13217) · Ensembl [ENSG00000102580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102580)

## Data

Gene col 2258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2258); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2258]; `tensor/DDL_lfc|DDL_z.npy` [2258]; `embed/gene_vectors.npy` [2258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2258 or target_col == 2258). Every well: [[DNAJC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
