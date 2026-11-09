---
symbol: "NANS"
type: "gene"
col: 1743
ensembl_id: "ENSG00000095380"
name: "N-acetylneuraminate synthase"
location: "9q22.33"
module: 56
arm: "+"
pooled_cpm: 46.99
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# NANS

*N-acetylneuraminate synthase* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +7.8, q 5e-12, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.652× (z -6.4, q 1e-07, down in 25 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.743× (z -6.3, q 1e-07, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDELR2]] (+0.73, fdr 7e-06), [[DHDDS]] (+0.73, fdr 7e-06), [[PDXDC1]] (+0.73, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +7.8 | 5e-12 | 34/48 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +7.1 | 3e-10 | 34/48 (Hs 766T, A-427, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 3e-09 | 32/48 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +6.0 | 3e-07 | 36/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 1e-05 | 27/47 (LS 180, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.20× | +3.8 | 0.015 | 16/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.027 | 24/48 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.035 | 21/48 (LS 180, COLO 205, …) | two highest doses | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.057 | 15/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -6.4 | 1e-07 | 25/48 (KATO III, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.743×** | -6.3 | 1e-07 | 37/48 (A498, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -5.1 | 7e-05 | 29/48 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.720×** | -4.9 | 1e-04 | 27/47 (LoVo, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.726×** | -4.4 | 0.001 | 26/42 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.004 | 24/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.774×** | -3.8 | 0.010 | 22/48 (NCI-H661, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.783×** | -3.6 | 0.019 | 23/48 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.020 | 23/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.022 | 20/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.022 | 19/48 (A549, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.5 | 0.025 | 24/48 (A498, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.034 | 20/48 (SW 900, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.035 | 19/48 (A498, RKO, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.051 | 16/48 (C32, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.058 | 17/48 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.058 | 18/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.070 | 16/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.084 | 17/47 (A498, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 85.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -10.7) |
| [[A498 (line)]] | wt | 107 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.591× (z -8.8) |
| [[HOP62 (line)]] | alt | 38.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.300× (z -9.8) |
| [[LoVo (line)]] | wt | 75.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 60.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 46.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0726× (z -8.7) |
| [[A-172 (line)]] | wt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 59.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +8.5) | — |
| [[J82 (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR2]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[DHDDS]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC1]] | +0.73 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.72 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[HM13]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[COG6]] | +0.72 | +0.61 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDIA5]] | +0.72 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SEC13]] | +0.72 | +0.58 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TXNDC11]] | +0.71 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.71 | +0.63 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 460 |
| [[GNL2]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NANS's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -33.5); signed map (-50.2, 10.4). **Vector** length 129, 37.0% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.59 to 16); *protein secretion* (hallmark, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +7.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.1 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.7 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.6 | +1.6 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylneuraminate synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,056,732-98,083,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAS |
| Reactome | 4 pathways, smallest: Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR45](https://www.uniprot.org/uniprotkb/Q9NR45) (N-acetylneuraminate-9-phosphate synthase):

> Catalyzes the condensation of phosphoenolpyruvate (PEP) and N-acetylmannosamine 6-phosphate (ManNAc-6-P) to synthesize N-acetylneuraminate-9-phosphate (Neu5Ac-9-P). Also catalyzes the condensation of PEP and D-mannose 6-phosphate (Man-6-P) to produce 3-deoxy-D-glycero-beta-D-galacto-non-2-ulopyranosonate 9-phosphate (KDN-9-P). Neu5Ac-9-P and KDN-9-P are the phosphorylated forms of sialic acids N-acetylneuraminic acid (Neu5Ac) and deaminoneuraminic acid (KDN), respectively. Required for brain …

**Summary**, from NCBI Gene [54187](https://www.ncbi.nlm.nih.gov/gene/54187):

> This gene encodes an enzyme that functions in the biosynthetic pathways of sialic acids. In vitro, the encoded protein uses N-acetylmannosamine 6-phosphate and mannose 6-phosphate as substrates to generate phosphorylated forms of N-acetylneuraminic acid (Neu5Ac) and 2-keto-3-deoxy-D-glycero-D-galacto-nononic acid (KDN), respectively; however, it exhibits much higher activity toward the Neu5Ac phosphate product. In insect cells, expression of this gene results in Neu5Ac and KDN production. This …

**Accessions** — [HGNC:19237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19237) · Entrez [54187](https://www.ncbi.nlm.nih.gov/gene/54187) · UniProt [Q9NR45](https://www.uniprot.org/uniprotkb/Q9NR45) · Ensembl [ENSG00000095380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095380)

## Data

Gene col 1743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1743); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1743]; `tensor/DDL_lfc|DDL_z.npy` [1743]; `embed/gene_vectors.npy` [1743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1743 or target_col == 1743). Every well: [[NANS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NANS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
