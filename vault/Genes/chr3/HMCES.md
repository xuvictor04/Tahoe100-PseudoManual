---
symbol: "HMCES"
type: "gene"
col: 11426
ensembl_id: "ENSG00000183624"
name: "5-hydroxymethylcytosine binding, ES cell specific"
location: "3q21.3"
module: 42
arm: "+"
pooled_cpm: 29.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# HMCES

*5-hydroxymethylcytosine binding, ES cell specific* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.44× (z +7.5, q 3e-11, up in 23 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 3.23×, SW480 2.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.21×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.686× (z -11.4, q 3e-27, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T2]] (+0.61, fdr 1e-05), [[SMARCD2]] (+0.61, fdr 3e-05), [[ODF2]] (+0.59, fdr 3e-05); moves opposite to [[USP40]] (-0.59, fdr 4e-05), [[CSTF2T]] (-0.59, fdr 2e-05), [[MOCS3]] (-0.57, fdr 6e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 12 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11426.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 3.23×, SW480 2.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.21×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.44×** | +7.5 | 3e-11 | 23/36 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.39×** | +7.1 | 4e-10 | 25/43 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.4 | 1e-05 | 20/45 (HCT15, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +5.4 | 1e-05 | 23/48 (SW480, HepG2/C3A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.25×** | +4.8 | 2e-04 | 23/46 (SW480, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.26×** | +4.5 | 5e-04 | 16/42 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +4.2 | 0.002 | 18/48 (PANC-1, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.22×** | +4.2 | 0.002 | 17/47 (RKO, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +4.2 | 0.002 | 16/48 (PANC-1, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.20×** | +3.9 | 0.005 | 16/48 (PANC-1, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | 1.19× | +3.6 | 0.016 | 17/47 (PANC-1, A-172, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +3.2 | 0.073 | 10/47 (PANC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.686×** | -11.4 | 3e-27 | 30/47 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -8.6 | 3e-15 | 36/48 (HS-578T, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -6.3 | 7e-08 | 23/48 (SW1417, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.758×** | -5.9 | 5e-07 | 21/47 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -5.3 | 1e-05 | 19/48 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -5.3 | 1e-05 | 21/47 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -4.6 | 3e-04 | 17/48 (H4, A-172, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.844× | -3.6 | 0.022 | 21/48 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.845× | -3.5 | 0.035 | 14/47 (HepG2/C3A, Hs 766T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.4 | 0.044 | 13/48 (LoVo, SHP-77, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.3 | 0.052 | 18/48 (A-172, hTERT-HPNE, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.863× | -3.1 | 0.078 | 9/47 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.905× | -3.0 | 0.12 | 6/48 (RPMI-7951, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 54.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -13.9) |
| [[A-427 (line)]] | wt | 52.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -14.5) |
| [[PANC-1 (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0723× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.9) |
| [[KATO III (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.8) |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -11.5) |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.6) |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[ODF2]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[AP2A1]] | +0.58 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[BCL7C]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SLC31A1]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[P3H1]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[SIVA1]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[GMCL1]] | +0.57 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[PI4KAP2]] | +0.57 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[MAD2L2]] | +0.56 | +0.39 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP40]] | -0.59 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[CSTF2T]] | -0.59 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[MOCS3]] | -0.57 | -0.67 / -0.39 | both halves | 6e-05 |  |
| [[ZNF462]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[METTL18]] | -0.56 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[SLX4IP]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC8]] | -0.55 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[FBXO38]] | -0.55 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[TRIM44]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[KICS2]] | -0.54 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[PSMD7]] | -0.53 | -0.58 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HMCES's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.4, 8.6); signed map (-46.9, -3.6). **Vector** length 78.4, 14.2% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +4.0 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.2 | +4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +2.9 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.9 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | 5-hydroxymethylcytosine binding, ES cell specific |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,278,828-129,306,186 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC12, SRAPD1; previously C3orf37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FZ2](https://www.uniprot.org/uniprotkb/Q96FZ2) (Abasic site processing protein HMCES):

> Sensor of abasic sites in single-stranded DNA (ssDNA) required to preserve genome integrity by promoting error-free repair of abasic sites. Acts as an enzyme that recognizes and binds abasic sites in ssDNA at replication forks and chemically modifies the lesion by forming a covalent cross-link with DNA: forms a stable thiazolidine linkage between a ring-opened abasic site and the alpha-amino and sulfhydryl substituents of its N-terminal catalytic cysteine residue. Promotes error-free repair by …

**Summary**, from NCBI Gene [56941](https://www.ncbi.nlm.nih.gov/gene/56941):

> Enables DNA-(abasic site) binding activity; protein-DNA covalent cross-linking activity; and single-stranded DNA binding activity. Involved in interstrand cross-link repair; protein-DNA covalent cross-linking repair; and somatic hypermutation of immunoglobulin genes. Is active in replication fork. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24446) · Entrez [56941](https://www.ncbi.nlm.nih.gov/gene/56941) · UniProt [Q96FZ2](https://www.uniprot.org/uniprotkb/Q96FZ2) · Ensembl [ENSG00000183624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183624)

## Data

Gene col 11426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11426); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11426]; `tensor/DDL_lfc|DDL_z.npy` [11426]; `embed/gene_vectors.npy` [11426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11426 or target_col == 11426). Every well: [[HMCES — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMCES.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
