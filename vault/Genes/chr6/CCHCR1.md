---
symbol: "CCHCR1"
type: "gene"
col: 12886
ensembl_id: "ENSG00000204536"
name: "coiled-coil alpha-helical rod protein 1"
location: "6p21.33"
module: 71
arm: "+"
pooled_cpm: 13.98
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# CCHCR1

*coiled-coil alpha-helical rod protein 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.55× (z +5.0, q 4e-04, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.587× (z -11.9, q 9e-30, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE19]] (+0.63, fdr 1e-05), [[DSN1]] (+0.59, fdr 1e-05), [[RAD54B]] (+0.57, fdr 1e-05); moves opposite to [[TNFRSF12A]] (-0.50, fdr 3e-05), [[RESF1]] (-0.47, fdr 6e-05), [[PHLDA2]] (-0.47, fdr 1e-04).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FANCI]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 4e-04 | 13/45 (Panc 03.27, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.6 | 0.001 | 11/24 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.22×** | +4.4 | 0.002 | 14/48 (J82, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.017 | 10/45 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.6 | 0.030 | 1/25 (J82) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.032 | 12/42 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.5 | 0.032 | 15/38 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.032 | 7/46 (HOP62, PANC-1, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.053 | 12/43 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +3.3 | 0.061 | 11/42 (HT-29, COLO 205, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.099 | 9/44 (KATO III, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | 1.23× | +3.0 | 0.10 | 9/32 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.10 | 9/46 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.11 | 5/48 (HEC-1-A, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.587×** | -11.9 | 9e-30 | 36/47 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -9.3 | 3e-18 | 27/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.561×** | -9.1 | 2e-17 | 27/45 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -8.9 | 6e-17 | 32/48 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -8.8 | 2e-16 | 31/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -7.4 | 1e-11 | 28/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.656×** | -6.6 | 3e-09 | 22/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -5.5 | 3e-06 | 23/47 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -4.7 | 2e-04 | 13/44 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 3e-04 | 17/47 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -4.0 | 0.004 | 14/47 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -3.6 | 0.016 | 12/47 (Panc 03.27, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -3.5 | 0.018 | 13/41 (COLO 205, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.043 | 13/47 (LS 180, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.199× (z -9.0) |
| [[H4 (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0831× (z -10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0965× (z -10.0) |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -11.0) |
| [[A498 (line)]] | wt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.2) |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 6.19 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0627× (z -8.9) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0737× (z -10.3) |
| [[J82 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.9) |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.218× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0801× (z -10.9) |
| [[SW480 (line)]] | alt | 12.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.309× (z -8.9) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE19]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DSN1]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RAD54B]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[HAUS5]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TMEM143]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[DDX12P]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[METTL17]] | +0.52 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[CDK5RAP3]] | +0.52 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[HAUS4]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[FSBP]] | +0.52 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[NUP85]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[RESF1]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[PHLDA2]] | -0.47 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[MSRA]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[HOMER1]] | -0.44 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[KIF26B]] | -0.44 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[RASGRF2]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SLC39A10]] | -0.44 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RAP2C-AS1]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[KDSR]] | -0.43 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[BICD1]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[LINC01033]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FANCI]] | C | FANCI's natural level strengthens CCHCR1's drug response | FANCI's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.36; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SPC24]] | C | SPC24's natural level strengthens CCHCR1's drug response | SPC24's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.30; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CCHCR1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CCHCR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.503 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.421). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.8, -49.3); signed map (-41.1, -40.6). **Vector** length 60.7, 9.04% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.1 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +5.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil alpha-helical rod protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,142,439-31,158,238 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCR; previously C6orf18 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD31](https://www.uniprot.org/uniprotkb/Q8TD31) (Coiled-coil alpha-helical rod protein 1):

> May be a regulator of keratinocyte proliferation or differentiation.

**Summary**, from NCBI Gene [54535](https://www.ncbi.nlm.nih.gov/gene/54535):

> This gene encodes a protein with five coiled-coil alpha-helical rod domains that is thought to act as a regulator of mRNA metabolism through its interaction with mRNA-decapping protein 4. It localizes to P-bodies, the site of mRNA metabolism, with an N-terminus that is required for this subcellular localization, suggesting it is a P-body component. Naturally occurring mutations in this gene are associated with psoriasis. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:13930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13930) · Entrez [54535](https://www.ncbi.nlm.nih.gov/gene/54535) · UniProt [Q8TD31](https://www.uniprot.org/uniprotkb/Q8TD31) · Ensembl [ENSG00000204536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204536)

## Data

Gene col 12886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12886); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12886]; `tensor/DDL_lfc|DDL_z.npy` [12886]; `embed/gene_vectors.npy` [12886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12886 or target_col == 12886). Every well: [[CCHCR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCHCR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
