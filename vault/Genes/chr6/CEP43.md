---
symbol: "CEP43"
type: "gene"
col: 13079
ensembl_id: "ENSG00000213066"
name: "centrosomal protein 43"
location: "6q27"
module: 67
arm: "+"
pooled_cpm: 64.64
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CEP43

*centrosomal protein 43* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.04× (z +15.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.479× (z -15.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OIP5]] (+0.66, fdr 8e-06), [[KIF22]] (+0.66, fdr 7e-06), [[SPAG5]] (+0.65, fdr 7e-06); moves opposite to [[NPL]] (-0.63, fdr 7e-06), [[GLRX2]] (-0.58, fdr 2e-05), [[RPF1]] (-0.57, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +15.4 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.5 | 1e-33 | 44/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +10.3 | 1e-22 | 40/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +10.3 | 1e-22 | 37/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +10.0 | 1e-21 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +7.3 | 4e-11 | 34/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +5.7 | 7e-07 | 28/49 (KATO III, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 5e-06 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +4.3 | 1e-03 | 21/47 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.9 | 0.005 | 13/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.31× | +3.1 | 0.11 | 13/48 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.12 | 3/47 (C32, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.479×** | -15.8 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.723×** | -9.8 | 2e-20 | 43/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.685×** | -8.1 | 8e-14 | 37/48 (NCI-H661, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -5.4 | 1e-05 | 28/48 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.004 | 23/48 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.831×** | -3.8 | 0.012 | 17/44 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.847× | -3.6 | 0.029 | 13/48 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.860× | -3.1 | 0.13 | 16/48 (J82, A-172, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 0.868× | -3.0 | 0.13 | 8/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.0 | 0.13 | 18/48 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.869× | -3.0 | 0.13 | 15/48 (HOP62, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.0 | 5 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +13.4) | [[Auranofin (drug)]] 5 µM 0.407× (z -11.6) |
| [[PANC-1 (line)]] | alt | 104 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +18.3) | [[Auranofin (drug)]] 5 µM 0.441× (z -11.1) |
| [[KATO III (line)]] | alt | 69.3 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.07× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +14.5) | [[Auranofin (drug)]] 5 µM 0.416× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 69.5 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.89× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.1) | — |
| [[LoVo (line)]] | wt | 53.5 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.406× (z -9.5) |
| [[SW480 (line)]] | alt | 90.8 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.380× (z -13.4) |
| [[LS 180 (line)]] | wt | 62.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +13.5) | — |
| [[C32 (line)]] | wt | 65.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.395× (z -9.5) |
| [[HOP62 (line)]] | alt | 73.9 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.394× (z -11.0) |
| [[HT-29 (line)]] | alt | 69.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0589× (z -10.1) |
| [[SHP-77 (line)]] | alt | 84.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.332× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 70.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.8) | — |
| [[SW48 (line)]] | wt | 73.4 | 0 | 2 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0809× (z -10.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.312× (z -9.1) |
| [[A-172 (line)]] | wt | 65.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.309× (z -12.8) |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.193× (z -10.8) |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.291× (z -8.6) |
| [[H4 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 70.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.200× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 84.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.462× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 45.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0578× (z -14.9) ⚠ toxic |
| [[RKO (line)]] | wt | 59.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 71.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.120× (z -8.8) |
| [[A-427 (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OIP5]] | +0.66 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[KIF22]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 | same gene group |
| [[ATL2]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[IFT122]] | +0.64 | +0.75 / +0.69 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[SKA2]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[TCTN3]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[CDCA3]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SPC25]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[CCP110]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 | same gene group; pathway: AURKA Activation by TPX2 |
| [[TDP1]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ARHGAP11B]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPL]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[GLRX2]] | -0.58 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[RPF1]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PHEX]] | -0.55 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RPLP0P2]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ALAS1]] | -0.55 | -0.59 / -0.48 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[ZFAND5]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[NABP1]] | -0.55 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[EIF6]] | -0.54 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[UBC]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 | pathway: G2/M Transition |
| [[BCL10]] | -0.53 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[LRIF1]] | -0.51 | -0.59 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises CEP43's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without PBK | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.7, -54.9); signed map (-47.4, -39.2). **Vector** length 116, 32.1% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 12); *G2/M checkpoint* (hallmark, mean cos +0.54 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +10.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +12.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.9 | +15.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.2 | +10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.5 | +10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.0 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.6 | -15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -9.5 | -9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:166,999,174-167,052,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FOP; previously FGFR1OP |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Reactome | 22 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [O95684](https://www.uniprot.org/uniprotkb/O95684) (Centrosomal protein 43):

> Required for anchoring microtubules to the centrosomes. Required for ciliation.

**Summary**, from NCBI Gene [11116](https://www.ncbi.nlm.nih.gov/gene/11116):

> This gene encodes a largely hydrophilic centrosomal protein that is required for anchoring microtubules to subcellular structures. A t(6;8)(q27;p11) chromosomal translocation, fusing this gene and the fibroblast growth factor receptor 1 (FGFR1) gene, has been found in cases of myeloproliferative disorder. The resulting chimeric protein contains the N-terminal leucine-rich region of this encoded protein fused to the catalytic domain of FGFR1. Alterations in this gene may also be associated with …

**Accessions** — [HGNC:17012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17012) · Entrez [11116](https://www.ncbi.nlm.nih.gov/gene/11116) · UniProt [O95684](https://www.uniprot.org/uniprotkb/O95684) · Ensembl [ENSG00000213066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213066)

## Data

Gene col 13079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13079); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13079]; `tensor/DDL_lfc|DDL_z.npy` [13079]; `embed/gene_vectors.npy` [13079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13079 or target_col == 13079). Every well: [[CEP43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
