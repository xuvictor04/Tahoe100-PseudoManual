---
symbol: "CA5BP1"
type: "gene"
col: 11803
ensembl_id: "ENSG00000186312"
name: "carbonic anhydrase 5B pseudogene 1"
location: "Xp22.2"
module: 40
arm: "+"
pooled_cpm: 11.49
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CA5BP1

*carbonic anhydrase 5B pseudogene 1* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.00× (z +9.8, q 8e-20, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.411× (z -15.2, q 0e+00, down in 31 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.743× (z -7.2, q 1e-10, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A9]] (+0.58, fdr 1e-05), [[DCAF11]] (+0.57, fdr 1e-05), [[STX5]] (+0.56, fdr 3e-05); moves opposite to [[RPAP3]] (-0.64, fdr 8e-06), [[MOCS2]] (-0.56, fdr 4e-05), [[PPID]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CA5B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +9.8 | 8e-20 | 33/47 (HOP62, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +9.7 | 9e-20 | 26/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.6 | 5e-12 | 24/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +6.8 | 1e-09 | 19/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +6.5 | 8e-09 | 21/43 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.7 | 1e-06 | 21/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.0 | 0.004 | 8/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.004 | 9/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.005 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.411×** | -15.2 | 0e+00 | 31/35 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -9.1 | 2e-17 | 16/20 (SW1417, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -7.2 | 1e-10 | 23/48 (A498, Hs 766T, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -7.2 | 1e-10 | 18/46 (NCI-H2347, HS-578T, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -7.0 | 3e-10 | 18/27 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -6.6 | 4e-09 | 23/43 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -6.1 | 7e-08 | 21/46 (BT-474, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.706×** | -5.7 | 8e-07 | 16/45 (NCI-H2347, HS-578T, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -5.3 | 8e-06 | 20/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -4.7 | 1e-04 | 18/47 (A-172, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.762×** | -4.6 | 2e-04 | 20/47 (A549, H4, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.775×** | -4.4 | 6e-04 | 16/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.614×** | -4.3 | 6e-04 | 9/47 (HS-578T, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.837× | -4.3 | 6e-04 | 12/48 (HT-29, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.811×** | -3.6 | 0.012 | 15/45 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.018 | 15/45 (HS-578T, AN3 CA, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.817×** | -3.5 | 0.018 | 11/43 (BT-474, Hs 766T, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 0.5 µM |  | **0.781×** | -3.0 | 0.063 | 6/46 (C32, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.063 | 10/46 (SW48, H4, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 17.9 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0294× (z -21.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0938× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 15.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.49× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 12.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.97 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0712× (z -13.4) |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0743× (z -15.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 8.40 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.168× (z -9.1) |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0392× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.121× (z -11.4) ⚠ transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 14.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.118× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -19.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 6.75 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0755× (z -8.7) |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A9]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DCAF11]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[STX5]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[RPN2]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZNF131]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SSR4]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ZNF487]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MGAT1]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.53 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[KDELR1]] | +0.53 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[CA5BP1-1]] | +0.53 | +0.73 / +0.43 | both halves | 3e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PRDX4]] | +0.53 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[MED26]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP3]] | -0.64 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[MOCS2]] | -0.56 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[PPID]] | -0.55 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[HUS1]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MPHOSPH6]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RNF180]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZNF780A]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PSMD6]] | -0.53 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ZNF354A]] | -0.52 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ALAS1]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RIPOR1]] | -0.52 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[NUDT9]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA5B]] | C | CA5BP1's natural level strengthens CA5B's drug response | CA5BP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.56; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-13.5, -19.6); signed map (-45.3, 15.0). **Vector** length 59.6, 8.20% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | +9.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.0 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +1.8 | +9.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +0.9 | +0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.8 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | carbonic anhydrase 5B pseudogene 1 |
| Locus type | pseudogene |
| Location | Xp22.2 — chrX:15,681,053-15,703,192 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | PRO2325; previously CA5BL, CA5BP |
| Matched by | ensembl_id |

UniProt [Q8WTZ4](https://www.uniprot.org/uniprotkb/Q8WTZ4) carries no function annotation.

**Summary**, from NCBI Gene [340591](https://www.ncbi.nlm.nih.gov/gene/340591):

> Predicted to enable carbonate dehydratase activity. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29544) · Entrez [340591](https://www.ncbi.nlm.nih.gov/gene/340591) · UniProt [Q8WTZ4](https://www.uniprot.org/uniprotkb/Q8WTZ4) · Ensembl [ENSG00000186312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186312)

## Data

Gene col 11803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11803); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11803]; `tensor/DDL_lfc|DDL_z.npy` [11803]; `embed/gene_vectors.npy` [11803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11803 or target_col == 11803). Every well: [[CA5BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA5BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
