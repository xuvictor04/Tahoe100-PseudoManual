---
symbol: "BMS1P4-1"
type: "gene"
col: 15695
ensembl_id: "ENSG00000271816"
name: ""
location: ""
module: 114
arm: "+"
pooled_cpm: 13.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# BMS1P4-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +12.0, q 3e-30, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.587× (z -8.5, q 1e-14, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGAP5]] (+0.78, fdr 7e-06, ⚠ same locus), [[MTG2]] (+0.77, fdr 7e-06), [[ZNF721]] (+0.70, fdr 7e-06), [[GOSR1]] (+0.70, fdr 1e-05); moves opposite to [[SNX30]] (-0.64, fdr 3e-05), [[HPSE]] (-0.64, fdr 5e-05), [[AIF1L]] (-0.60, fdr 1e-04).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02987]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +12.0 | 3e-30 | 34/46 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.1 | 4e-10 | 24/41 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.0 | 6e-10 | 22/48 (A-427, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +6.4 | 2e-08 | 26/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.1 | 1e-07 | 23/46 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 4e-07 | 22/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.35×** | +4.8 | 1e-04 | 17/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.5 | 4e-04 | 16/47 (HOP62, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 18/47 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.004 | 9/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.006 | 7/47 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.5 | 0.025 | 7/30 (LS 180, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.035 | 5/42 (SK-MEL-2, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.035 | 5/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.3 | 0.040 | 7/45 (LoVo, PANC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.080 | 5/47 (A498, SW1417, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.080 | 8/47 (NCI-H2347, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.587×** | -8.5 | 1e-14 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -8.4 | 2e-14 | 25/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.586×** | -8.2 | 4e-14 | 27/40 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -7.9 | 3e-13 | 26/46 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -7.3 | 4e-11 | 23/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -4.3 | 0.002 | 13/26 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.793×** | -3.6 | 0.024 | 5/47 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.654×** | -3.6 | 0.024 | 7/43 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.800×** | -3.6 | 0.024 | 18/42 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.0 | 0.15 | 10/48 (CHP-212, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.251× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -10.2) |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.222× (z -13.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -13.0) |
| [[SW480 (line)]] | alt | 21.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -8.8) |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0650× (z -14.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0976× (z -14.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.293× (z -9.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 6.72 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0772× (z -11.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -11.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 7.69 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0735× (z -12.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 18.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0933× (z -9.9) |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP5]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[MTG2]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.70 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[GOSR1]] | +0.70 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[BMS1P4]] | +0.68 | +0.66 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NMNAT1]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TRAPPC13]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.62 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[C2orf42]] | +0.62 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[LAMB2P1]] | +0.61 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[MTERF4]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ZNF547]] | +0.61 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ZNF785]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX30]] | -0.64 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[HPSE]] | -0.64 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[AIF1L]] | -0.60 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[CREG1]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TWSG1]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[MGAT4A]] | -0.56 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[HMG20B]] | -0.56 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.56 | -0.64 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[IL17RD]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ARRB2]] | -0.54 | -0.56 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[VPS13A]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02987]] | B | LINC02987 activity lowers BMS1P4-1's level | lines that do not express LINC02987 (5) vs lines expressing it (45) | 1.51× higher at baseline in the lines without LINC02987 | 0.042 | ⚠ within organs, on part of the lines; also absent: NME4, ZNF566, SPIRE1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.5, 6.2); signed map (-3.9, -14.0). **Vector** length 71.4, 11.7% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +7.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.5 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | -3.6 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.2 | +0.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

> [!warning] No registry record
> BMS1P4-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15695); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15695]; `tensor/DDL_lfc|DDL_z.npy` [15695]; `embed/gene_vectors.npy` [15695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15695 or target_col == 15695). Every well: [[BMS1P4-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1P4-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
