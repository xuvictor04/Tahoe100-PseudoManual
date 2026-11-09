---
symbol: "RHOC"
type: "gene"
col: 7891
ensembl_id: "ENSG00000155366"
name: "ras homolog family member C"
location: "1p13.2"
module: 184
arm: "+"
pooled_cpm: 33.17
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# RHOC

*ras homolog family member C* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +11.8, q 3e-29, up in 40 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.34× (z +4.5, q 4e-04, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -10.7, q 6e-24, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOVL1]] (+0.70, fdr 7e-06), [[ORMDL2]] (+0.61, fdr 1e-05), [[CAPN2]] (+0.59, fdr 7e-06); moves opposite to [[RBM26]] (-0.58, fdr 2e-05), [[PRPF4B]] (-0.57, fdr 1e-05), [[SREK1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CD59]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +11.8 | 3e-29 | 40/41 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +8.8 | 3e-16 | 32/35 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.4 | 3e-11 | 30/37 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.74×** | +6.1 | 2e-07 | 33/45 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.64×** | +5.4 | 8e-06 | 33/45 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.60×** | +5.2 | 2e-05 | 28/46 (LoVo, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.7 | 2e-04 | 1/46 (NCI-H1573) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +4.5 | 4e-04 | 22/46 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.78×** | +4.5 | 4e-04 | 29/46 (HT-29, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 7e-04 | 25/45 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +4.3 | 8e-04 | 24/45 (NCI-H460, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.003 | 28/45 (HT-29, COLO 205, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.003 | 31/46 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.006 | 24/45 (NCI-H460, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.006 | 23/46 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.021 | 23/44 (RKO, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.021 | 18/46 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.031 | 16/46 (HT-29, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -10.7 | 6e-24 | 37/45 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.707×** | -3.9 | 0.030 | 22/46 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.798×** | -3.6 | 0.062 | 27/46 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Trimetrexate (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.075 | 21/46 (Hs 766T, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.757× | -3.1 | 0.20 | 16/46 (NCI-H460, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 78.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -12.6) |
| [[A498 (line)]] | wt | 61.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +11.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 71.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.4) |
| [[HOP62 (line)]] | alt | 22.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.4) |
| [[HS-578T (line)]] | alt | 75.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 46.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 47.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 23.8 | 1 | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.51× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.2) |
| [[SNU-423 (line)]] | alt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 58.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +11.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 1 | — | [[crizotinib (drug)]] 5 µM 0.0533× (z -9.0) |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 1 | — | [[Afatinib (drug)]] 5 µM 0.223× (z -9.6) |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0858× (z -9.9) |
| [[C32 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.7) |
| [[HT-29 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -8.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[J82 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.3) |
| [[LoVo (line)]] | wt | 28.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 40.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.6) |
| [[PANC-1 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL1]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ORMDL2]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.59 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LRP10]] | +0.59 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CD59]] | +0.56 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SERINC2]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DYNLT1]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CAP1]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DYNLT3]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RALB]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ARPC5]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 | pathway: RHO GTPase Effectors |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PRPF4B]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SREK1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[LUC7L2]] | -0.53 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[RPRD2]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZZZ3]] | -0.51 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[CYB5RL]] | -0.50 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[PTBP2]] | -0.50 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[PUM2]] | -0.50 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[GOLGA2P5]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PNISR]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ACBD6]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises RHOC's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.22× lower at baseline in the lines without CD59 | 0.022 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (15.2, -1.2); signed map (-6.0, 40.1). **Vector** length 96.3, 26.9% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.8 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.4 | +4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +4.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Darinaparsin (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,701,127-112,707,434 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARH9, ARHC |
| Gene groups (HGNC) | Rho family GTPases |
| Reactome | 18 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; RHO GTPases Activate ROCKs; RHO GTPases activate CIT |
| Matched by | ensembl_id |

**Function**, from UniProt [P08134](https://www.uniprot.org/uniprotkb/P08134) (Rho-related GTP-binding protein RhoC):

> Regulates a signal transduction pathway linking plasma membrane receptors to the assembly of focal adhesions and actin stress fibers. Serves as a microtubule-dependent signal that is required for the myosin contractile ring formation during cell cycle cytokinesis. Regulates apical junction formation in bronchial epithelial cells.

**Summary**, from NCBI Gene [389](https://www.ncbi.nlm.nih.gov/gene/389):

> This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The protein encoded by this gene is prenylated at its C-terminus, and localizes to the cytoplasm and plasma membrane. It is thought to be important in cell locomotion. Overexpression of …

**Accessions** — [HGNC:669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:669) · Entrez [389](https://www.ncbi.nlm.nih.gov/gene/389) · UniProt [P08134](https://www.uniprot.org/uniprotkb/P08134) · Ensembl [ENSG00000155366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155366)

## Data

Gene col 7891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7891); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7891]; `tensor/DDL_lfc|DDL_z.npy` [7891]; `embed/gene_vectors.npy` [7891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7891 or target_col == 7891). Every well: [[RHOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
