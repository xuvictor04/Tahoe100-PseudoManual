---
symbol: "AVIL"
type: "gene"
col: 5699
ensembl_id: "ENSG00000135407"
name: "advillin"
location: "12q14.1"
module: 38
arm: "+"
pooled_cpm: 19.92
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 39
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# AVIL

*advillin* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +7.8, q 3e-12, up in 39 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 3.50×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.167× (z -14.5, q 7e-45, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRA]] (+0.82, fdr 7e-06), [[GARIN1A]] (+0.79, fdr 7e-06), [[PYGM]] (+0.79, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP1LC3A]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5699.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 3.50×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +7.8 | 3e-12 | 39/45 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.88×** | +5.2 | 7e-05 | 31/47 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.47× | +3.2 | 0.24 | 17/47 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.30× | +3.0 | 0.24 | 12/47 (hTERT-HPNE, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.167×** | -14.5 | 7e-45 | 43/47 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.175×** | -14.1 | 7e-43 | 42/46 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.193×** | -13.3 | 4e-38 | 44/46 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.223×** | -12.2 | 8e-32 | 46/47 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.318×** | -9.3 | 2e-18 | 38/46 (SW 900, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.340×** | -8.4 | 4e-15 | 32/45 (HT-29, NCI-H23, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.411×** | -7.2 | 5e-11 | 37/47 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.441×** | -6.4 | 1e-08 | 32/47 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.455×** | -6.4 | 1e-08 | 36/47 (NCI-H1573, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.449×** | -6.3 | 2e-08 | 29/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.429×** | -6.1 | 7e-08 | 36/47 (NCI-H1792, LoVo, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.458×** | -6.0 | 1e-07 | 36/47 (SNU-423, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.495×** | -5.7 | 6e-07 | 29/47 (LOX-IMVI, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.494×** | -5.3 | 6e-06 | 31/46 (H4, A498, …) | all doses, flat | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.303×** | -5.0 | 2e-05 | 35/47 (NCI-H1792, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.543×** | -4.9 | 3e-05 | 28/46 (BT-474, A-427, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.568×** | -4.6 | 2e-04 | 31/47 (A549, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.577×** | -4.3 | 6e-04 | 25/47 (NCI-H1573, A-427, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.366×** | -4.2 | 6e-04 | 23/46 (NCI-H1792, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.0 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0791× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 71.2 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0921× (z -12.2) |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0573× (z -12.2) |
| [[SW 900 (line)]] | alt | 31.5 | 0 | 8 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0396× (z -15.5) ⚠ transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.111× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0555× (z -14.5) |
| [[A-427 (line)]] | wt | 30.5 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0498× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0226× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0781× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 41.6 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0834× (z -13.0) |
| [[H4 (line)]] | wt | 22.0 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0289× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0586× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0790× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0989× (z -9.5) |
| [[LoVo (line)]] | wt | 35.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0629× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -11.7) |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0739× (z -12.7) |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 3 | — | [[Digitoxin (drug)]] 0.05 µM 0.0805× (z -11.4) |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.104× (z -9.4) |
| [[KATO III (line)]] | alt | 19.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0534× (z -12.0) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.115× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0972× (z -10.5) |
| [[A549 (line)]] | wt | 15.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.103× (z -9.3) |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.0696× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0808× (z -10.6) |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0380× (z -13.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0924× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 7.84 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.129× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0521× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0997× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0835× (z -9.3) |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0868× (z -10.1) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRA]] | +0.82 | +0.80 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[GARIN1A]] | +0.79 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[PYGM]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[LINC00672]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.76 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[USP50]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[VWCE]] | +0.73 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[C21orf91-OT1]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1LC3A]] | C | MAP1LC3A activity raises AVIL's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 2.46× lower at baseline in the lines without MAP1LC3A | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent |
| [[SMBD1P]] | C | SMBD1P activity raises AVIL's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without SMBD1P | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, -16.7); signed map (15.3, 10.7). **Vector** length 118, 36.8% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.1 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.5 | -13.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -14.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -5.3 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -12.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | advillin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,797,376-57,818,734 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p92, FLJ12386, ADVIL, DOC6 |
| Gene groups (HGNC) | Gelsolin/villins |
| Matched by | ensembl_id |

**Function**, from UniProt [O75366](https://www.uniprot.org/uniprotkb/O75366) (Advillin):

> Ca(2+)-regulated actin-binding protein which plays an important role in actin bundling. May have a unique function in the morphogenesis of neuronal cells which form ganglia. Required for SREC1-mediated regulation of neurite-like outgrowth. Plays a role in regenerative sensory axon outgrowth and remodeling processes after peripheral injury in neonates. Involved in the formation of long fine actin-containing filopodia-like structures in fibroblast. Plays a role in ciliogenesis. In podocytes, …

**Summary**, from NCBI Gene [10677](https://www.ncbi.nlm.nih.gov/gene/10677):

> The protein encoded by this gene is a member of the gelsolin/villin family of actin regulatory proteins. This protein has structural similarity to villin. It binds actin and may play a role in the development of neuronal cells that form ganglia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14188) · Entrez [10677](https://www.ncbi.nlm.nih.gov/gene/10677) · UniProt [O75366](https://www.uniprot.org/uniprotkb/O75366) · Ensembl [ENSG00000135407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135407)

## Data

Gene col 5699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5699); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5699]; `tensor/DDL_lfc|DDL_z.npy` [5699]; `embed/gene_vectors.npy` [5699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5699 or target_col == 5699). Every well: [[AVIL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AVIL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
