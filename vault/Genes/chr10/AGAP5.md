---
symbol: "AGAP5"
type: "gene"
col: 10277
ensembl_id: "ENSG00000172650"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 5"
location: "10q22.2"
module: 37
arm: "+"
pooled_cpm: 4.65
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# AGAP5

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 5* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +7.9, q 1e-12, up in 26 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.557× (z -7.3, q 2e-10, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.124×, SW480 0.143×, AsPC-1 0.0536×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0465×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.205×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A498 0.0804×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1P4-1]] (+0.78, fdr 7e-06, ⚠ same locus), [[LYG1]] (+0.69, fdr 7e-06), [[TMED6]] (+0.66, fdr 7e-06), [[TRAPPC12]] (+0.66, fdr 7e-06); moves opposite to [[TPPP]] (-0.56, fdr 3e-04), [[TWSG1]] (-0.53, fdr 3e-05), [[CHML]] (-0.52, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.9 | 1e-12 | 26/38 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +7.0 | 9e-10 | 10/22 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.8 | 1e-06 | 13/34 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 2e-04 | 9/46 (HOP62, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +4.8 | 2e-04 | 14/46 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +4.1 | 0.003 | 4/44 (SW48, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.004 | 5/43 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +3.6 | 0.025 | 5/46 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.028 | 8/46 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.078 | 4/38 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +3.2 | 0.078 | 3/45 (SNU-423, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10277.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.124×, SW480 0.143×, AsPC-1 0.0536×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0465×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.205×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A498 0.0804×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -7.3 | 2e-10 | 22/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -6.2 | 2e-07 | 16/36 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -5.2 | 3e-05 | 18/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.703×** | -3.8 | 0.018 | 13/43 (BT-474, AsPC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.750×** | -3.6 | 0.041 | 18/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.736×** | -3.3 | 0.081 | 13/29 (LoVo, HCT15, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.27 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0465× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -13.9) |
| [[A498 (line)]] | wt | 4.40 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0804× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 3.41 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0536× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 3.23 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0692× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 7.49 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.170× (z -8.5) |
| [[SW1417 (line)]] | alt | 3.25 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0640× (z -8.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 8.18 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -12.6) |
| [[A-172 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P4-1]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[LYG1]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TMED6]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC12]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[AGAP6]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 | same gene group; STRING 531 |
| [[GOSR2]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[KLRA1P]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[GCNA]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ISY1-RAB43]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.61 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[APTX]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPPP]] | -0.56 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[TWSG1]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CHML]] | -0.52 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[MPP7]] | -0.52 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[SNX30]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[CXADR]] | -0.52 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.51 | -0.54 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AGAP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DDX59-AS1]] | B | DDX59-AS1 activity raises AGAP5's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without DDX59-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.3, -19.4); signed map (11.5, 9.8). **Vector** length 48.3, 5.52% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +1.8 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +4.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Adenine (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,674,287-73,698,109 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Em:AC073389.1; previously CTGLF2 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NIR3](https://www.uniprot.org/uniprotkb/A6NIR3) (Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 5):

> Putative GTPase-activating protein.

**Summary**, from NCBI Gene [729092](https://www.ncbi.nlm.nih.gov/gene/729092):

> Predicted to enable GTPase activator activity and GTPase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23467) · Entrez [729092](https://www.ncbi.nlm.nih.gov/gene/729092) · UniProt [A6NIR3](https://www.uniprot.org/uniprotkb/A6NIR3) · Ensembl [ENSG00000172650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172650)

## Data

Gene col 10277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10277); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10277]; `tensor/DDL_lfc|DDL_z.npy` [10277]; `embed/gene_vectors.npy` [10277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10277 or target_col == 10277). Every well: [[AGAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
