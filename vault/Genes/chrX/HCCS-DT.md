---
symbol: "HCCS-DT"
type: "gene"
col: 13939
ensembl_id: "ENSG00000234129"
name: "HCCS divergent transcript"
location: "Xp22.2"
module: 22
arm: "+"
pooled_cpm: 51.12
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HCCS-DT

*HCCS divergent transcript* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.56× (z +4.9, q 5e-04, up in 31 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 2.90×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.294× (z -13.6, q 2e-39, down in 43 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.313× (z -12.9, q 9e-36, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01572]] (+0.77, fdr 7e-06), [[KIF15]] (+0.74, fdr 7e-06), [[BIRC5]] (+0.72, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WWOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13939.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 2.90×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.9 | 5e-04 | 31/46 (SHP-77, SNU-423, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.34× | +3.2 | 0.26 | 12/46 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.33× | +3.1 | 0.26 | 17/46 (LS 180, HCT15, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.22× | +3.1 | 0.26 | 15/46 (SW 900, SW480, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.39× | +3.0 | 0.26 | 20/46 (KATO III, BT-474, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.294×** | -13.6 | 2e-39 | 43/46 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.313×** | -12.9 | 9e-36 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.324×** | -12.1 | 4e-31 | 39/43 (HCT15, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.384×** | -10.6 | 3e-24 | 42/46 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.422×** | -9.6 | 9e-20 | 43/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.415×** | -9.2 | 3e-18 | 42/46 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.439×** | -9.1 | 5e-18 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.223×** | -8.7 | 2e-16 | 38/46 (HOP62, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.575×** | -8.7 | 2e-16 | 32/46 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.224×** | -8.7 | 2e-16 | 42/46 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -8.5 | 9e-16 | 37/46 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.471×** | -8.0 | 4e-14 | 30/45 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -7.6 | 9e-13 | 29/46 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -6.7 | 9e-10 | 35/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.741×** | -4.7 | 9e-05 | 30/46 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -4.4 | 3e-04 | 26/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.663×** | -4.2 | 8e-04 | 24/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.667×** | -3.7 | 0.005 | 21/46 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.1 | 0 | 14 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -14.9) |
| [[A-427 (line)]] | wt | 153 | 0 | 13 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0622× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0434× (z -15.3) |
| [[SW480 (line)]] | alt | 85.4 | 0 | 12 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -16.7) |
| [[PANC-1 (line)]] | alt | 36.1 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.131× (z -15.3) |
| [[KATO III (line)]] | alt | 78.7 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 79.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.0) |
| [[COLO 205 (line)]] | alt | 47.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -11.7) |
| [[J82 (line)]] | alt | 49.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -9.9) |
| [[HCT15 (line)]] | alt | 56.9 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -12.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.177× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 70.3 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.262× (z -11.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.0) |
| [[HOP62 (line)]] | alt | 45.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.1) |
| [[LS 180 (line)]] | wt | 56.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -13.0) |
| [[A498 (line)]] | wt | 39.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.0) |
| [[LoVo (line)]] | wt | 35.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 48.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -13.3) |
| [[C-33 A (line)]] | alt | 70.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -11.9) |
| [[SHP-77 (line)]] | alt | 50.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -8.6) |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -11.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -10.9) |
| [[A549 (line)]] | wt | 53.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -13.0) |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -9.4) |
| [[Hs 766T (line)]] | wt | 42.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 82.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 81.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 83.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.0) |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.124× (z -9.4) |
| [[SW48 (line)]] | wt | 45.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.132× (z -9.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.164× (z -8.5) |
| [[BT-474 (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.8) | — |
| [[C32 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -10.7) ⚠ toxic |
| [[H4 (line)]] | wt | 67.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0232× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0808× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.114× (z -8.8) |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01572]] | +0.77 | +0.84 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KIF15]] | +0.74 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[MIR924HG]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[KIF11]] | +0.71 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[PRC1]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[PLK4]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MKI67]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[DIAPH3]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[SMC4]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TPX2]] | +0.69 | +0.76 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | B | WWOX activity raises HCCS-DT's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without WWOX | 0.062 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises HCCS-DT's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.95× lower at baseline in the lines without NDC80 | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, -53.0); signed map (-46.9, -44.6). **Vector** length 100, 33.4% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.55 to 60); *DREAM G2/M down* (control, mean cos +0.60 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.52 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +4.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.6 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.3 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.1 | +1.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.1 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -12.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.9 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HCCS divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xp22.2 — chrX:10,847,578-11,111,220 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55698) · Entrez [121847985](https://www.ncbi.nlm.nih.gov/gene/121847985) · Ensembl [ENSG00000234129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234129)

## Data

Gene col 13939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13939); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13939]; `tensor/DDL_lfc|DDL_z.npy` [13939]; `embed/gene_vectors.npy` [13939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13939 or target_col == 13939). Every well: [[HCCS-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCCS-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
