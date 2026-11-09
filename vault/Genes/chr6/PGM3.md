---
symbol: "PGM3"
type: "gene"
col: 271
ensembl_id: "ENSG00000013375"
name: "phosphoglucomutase 3"
location: "6q14.1"
module: 56
arm: "+"
pooled_cpm: 149.27
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PGM3

*phosphoglucomutase 3* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.55× (z +7.3, q 2e-10, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.544× (z -10.1, q 3e-21, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.701× (z -7.2, q 1e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDELR2]] (+0.84, fdr 7e-06), [[SEC24D]] (+0.83, fdr 7e-06), [[TMEM263]] (+0.83, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FBXO16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.3 | 2e-10 | 37/48 (HT-29, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 4e-04 | 25/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.078 | 25/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.44× | +3.2 | 0.19 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -10.1 | 3e-21 | 39/49 (HS-578T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -8.6 | 3e-15 | 28/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.624×** | -7.2 | 8e-11 | 34/45 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.701×** | -7.2 | 1e-10 | 36/48 (A498, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.646×** | -7.0 | 4e-10 | 43/48 (HS-578T, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -6.2 | 7e-08 | 4/50 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -5.3 | 1e-05 | 31/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.720×** | -5.2 | 1e-05 | 32/48 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.782×** | -4.1 | 0.003 | 25/48 (SW48, H4, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -4.0 | 0.004 | 28/48 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.788×** | -3.9 | 0.004 | 28/48 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.769×** | -3.9 | 0.005 | 29/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.764×** | -3.9 | 0.005 | 27/47 (C32, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.005 | 23/48 (hTERT-HPNE, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.781×** | -3.7 | 0.009 | 28/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.7 | 0.009 | 25/47 (LoVo, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.788×** | -3.5 | 0.014 | 26/49 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.811×** | -3.5 | 0.017 | 26/48 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.797×** | -3.4 | 0.022 | 26/48 (H4, COLO 205, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.037 | 25/49 (HT-29, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 129 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.311× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 171 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.8) |
| [[A-172 (line)]] | wt | 177 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 211 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.657× (z -10.1) |
| [[HS-578T (line)]] | alt | 283 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.524× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.431× (z -10.6) |
| [[HT-29 (line)]] | alt | 202 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.10× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 208 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.368× (z -9.6) |
| [[H4 (line)]] | wt | 202 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.04× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.306× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[C32 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 90.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.0) |
| [[COLO 205 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -9.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 228 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 66.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.94× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.174× (z -9.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 252 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 272 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 172 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR2]] | +0.84 | +0.85 / +0.85 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC24D]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[TMEM263]] | +0.83 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[DNAJC25]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[SRP54]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 | STRING 416 |
| [[COG6]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC31A]] | +0.79 | +0.79 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SERP1]] | +0.78 | +0.71 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ERLEC1]] | +0.78 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.77 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[COPB1]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPA]] | +0.77 | +0.72 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO16]] | B | FBXO16 activity lowers PGM3's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.43× higher at baseline in the lines without FBXO16 | 0.058 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -34.9); signed map (-50.9, 12.0). **Vector** length 158, 55.9% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.71 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.71 to 16); *protein secretion* (hallmark, mean cos +0.66 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.6 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.3 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.2 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglucomutase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:83,147,324-83,193,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AGM1, DKFZP434B187, PAGM |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 4 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [O95394](https://www.uniprot.org/uniprotkb/O95394) (Phosphoacetylglucosamine mutase):

> Catalyzes the conversion of GlcNAc-6-P into GlcNAc-1-P during the synthesis of uridine diphosphate/UDP-GlcNAc, a sugar nucleotide critical to multiple glycosylation pathways including protein N- and O-glycosylation.

**Summary**, from NCBI Gene [5238](https://www.ncbi.nlm.nih.gov/gene/5238):

> This gene encodes a member of the phosphohexose mutase family. The encoded protein mediates both glycogen formation and utilization by catalyzing the interconversion of glucose-1-phosphate and glucose-6-phosphate. A non-synonymous single nucleotide polymorphism in this gene may play a role in resistance to diabetic nephropathy and neuropathy. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:8907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8907) · Entrez [5238](https://www.ncbi.nlm.nih.gov/gene/5238) · UniProt [O95394](https://www.uniprot.org/uniprotkb/O95394) · Ensembl [ENSG00000013375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013375)

## Data

Gene col 271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 271); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 271]; `tensor/DDL_lfc|DDL_z.npy` [271]; `embed/gene_vectors.npy` [271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 271 or target_col == 271). Every well: [[PGM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
