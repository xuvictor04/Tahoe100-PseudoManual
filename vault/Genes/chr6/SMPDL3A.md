---
symbol: "SMPDL3A"
type: "gene"
col: 10273
ensembl_id: "ENSG00000172594"
name: "sphingomyelin phosphodiesterase acid like 3A"
location: "6q22.31"
module: 171
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# SMPDL3A

*sphingomyelin phosphodiesterase acid like 3A* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.59× (z +6.7, q 1e-08, up in 14 of 42 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.51× (z +4.2, q 0.003, up in 8 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.371× (z -10.3, q 5e-22, down in 28 of 42 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.689× (z -3.9, q 0.008, down in 12 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM94]] (+0.58, fdr 1e-05), [[ABHD4]] (+0.58, fdr 2e-05), [[FBXO7]] (+0.58, fdr 1e-05); moves opposite to [[TAF1B]] (-0.61, fdr 1e-05), [[CCDC57]] (-0.61, fdr 1e-05), [[SMARCA4]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLSCR4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.59×** | +6.7 | 1e-08 | 14/42 (LS 180, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.6 | 6e-06 | 1/10 (HT-29) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.8 | 3e-04 | 1/9 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.003 | 8/44 (A-427, HOP62, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.003 | 9/28 (LS 180, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.40×** | +3.4 | 0.055 | 9/37 (LS 180, A498, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.4 | 0.064 | 1/9 (KATO III) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.071 | 6/40 (A498, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.071 | 10/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.371×** | -10.3 | 5e-22 | 28/42 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.422×** | -8.9 | 1e-16 | 25/43 (KATO III, SHP-77, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.498×** | -7.2 | 1e-10 | 20/43 (AsPC-1, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.511×** | -7.0 | 5e-10 | 18/41 (A498, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.664×** | -4.2 | 0.002 | 17/39 (AsPC-1, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.664×** | -4.2 | 0.002 | 11/42 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.678×** | -3.9 | 0.008 | 16/39 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.689×** | -3.9 | 0.008 | 12/40 (SK-MEL-2, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.694×** | -3.8 | 0.009 | 8/43 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.509×** | -3.7 | 0.014 | 14/29 (SHP-77, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.530×** | -3.4 | 0.030 | 3/37 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 0.5 µM |  | **0.741×** | -3.1 | 0.087 | 6/37 (SHP-77, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.5 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 3.46 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vilanterol (drug)]] 0.5 µM 0.0754× (z -8.8) |
| [[KATO III (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0797× (z -9.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[COLO 205 (line)]] | alt | 4.89 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0458× (z -8.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 5.24 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0911× (z -8.5) |
| [[SNU-423 (line)]] | alt | 7.67 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -8.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM94]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ABHD4]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[FBXO7]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NAXD]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MKRN1]] | +0.56 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NADK2]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CLK1]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.53 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[RTCA]] | +0.53 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[RTCA-AS1]] | +0.53 | +0.41 / +0.32 | both halves | 2e-04 |  |
| [[TMEM59]] | +0.52 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF1B]] | -0.61 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CCDC57]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SMARCA4]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SERBP1]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PITPNB]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MAP3K14]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PFN1]] | -0.51 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[ADARB1]] | -0.51 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[SCART1]] | -0.50 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[WWC2]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[AGAP1]] | -0.49 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[NUP98]] | -0.49 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR4]] | B | PLSCR4 activity raises SMPDL3A's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without PLSCR4 | 0.044 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-2.4, -39.0); signed map (-30.2, -21.5). **Vector** length 59.2, 8.67% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.4 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.4 | -8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.3 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.1 | -7.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase acid like 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:122,789,049-122,809,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20177, ASM3A, ASML3a, yR36GH4.1 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92484](https://www.uniprot.org/uniprotkb/Q92484) (Cyclic GMP-AMP phosphodiesterase SMPDL3A):

> Cyclic-nucleotide phosphodiesterase that acts as a negative regulator of innate immunity by mediating degradation of 2',3'-cGAMP, thereby inhibiting the cGAS-STING signaling. Specifically linearizes 2',3'-cGAMP into 2'5'-bond pGpA and further hydrolyzes pGpA to produce GpA. Also has in vitro nucleotide phosphodiesterase activity with nucleoside triphosphates, such as ATP. Has in vitro activity with p-nitrophenyl-TMP. Has lower activity with nucleoside diphosphates, and no activity with …

**Summary**, from NCBI Gene [10924](https://www.ncbi.nlm.nih.gov/gene/10924):

> Enables phosphoric diester hydrolase activity and zinc ion binding activity. Involved in negative regulation of cGAS/STING signaling pathway and nucleoside triphosphate catabolic process. Located in extracellular exosome. Is active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17389) · Entrez [10924](https://www.ncbi.nlm.nih.gov/gene/10924) · UniProt [Q92484](https://www.uniprot.org/uniprotkb/Q92484) · Ensembl [ENSG00000172594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172594)

## Data

Gene col 10273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10273); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10273]; `tensor/DDL_lfc|DDL_z.npy` [10273]; `embed/gene_vectors.npy` [10273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10273 or target_col == 10273). Every well: [[SMPDL3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPDL3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
