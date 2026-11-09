---
symbol: "SMBD1P"
type: "gene"
col: 16026
ensembl_id: "ENSG00000283426"
name: "somatomedin B domain containing 1, pseudogene"
location: "3q29"
module: 38
arm: "+"
pooled_cpm: 20.6
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SMBD1P

*somatomedin B domain containing 1, pseudogene* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +5.2, q 1e-04, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.383× (z -9.5, q 2e-18, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC20-OT1]] (+0.88, fdr 7e-06, ⚠ same locus), [[UBE2CP5]] (+0.75, fdr 7e-06), [[NOXRED1]] (+0.70, fdr 7e-06), [[SLC23A3]] (+0.69, fdr 7e-06); moves opposite to [[LANCL1]] (-0.60, fdr 1e-05), [[SSX2IP]] (-0.57, fdr 1e-05), [[ZDHHC21]] (-0.55, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MUC20]] → it (grade B ⚠); 8 go from it, the strongest it → [[AADAT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-04 | 25/43 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.023 | 20/43 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.052 | 19/45 (A498, Panc 03.27, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.20 | 14/45 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.20 | 11/44 (A-427, NCI-H1792, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -9.5 | 2e-18 | 35/45 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.445×** | -7.7 | 6e-12 | 32/44 (AsPC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.469×** | -7.4 | 2e-11 | 31/43 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.257×** | -7.0 | 4e-10 | 35/45 (COLO 205, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.608×** | -6.9 | 5e-10 | 28/43 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.505×** | -6.7 | 2e-09 | 30/43 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -6.6 | 4e-09 | 31/44 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.572×** | -5.5 | 3e-06 | 28/44 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -5.3 | 7e-06 | 25/43 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.358×** | -5.3 | 7e-06 | 24/41 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -4.8 | 8e-05 | 23/43 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.649×** | -4.1 | 0.002 | 22/40 (COLO 205, J82, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.669×** | -3.9 | 0.003 | 22/38 (COLO 205, SW480, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.708×** | -3.4 | 0.029 | 19/44 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.713×** | -3.3 | 0.035 | 18/44 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.050 | 20/44 (A-427, SW 900, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 227 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0398× (z -28.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 38.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -9.2) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -10.1) |
| [[A549 (line)]] | wt | 16.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.100× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -10.8) |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -8.9) |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.9) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0632× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -14.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[H4 (line)]] | wt | 19.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0902× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 78.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.121× (z -9.4) |
| [[KATO III (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0921× (z -13.0) |
| [[LoVo (line)]] | wt | 23.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0681× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0831× (z -13.8) |
| [[A-172 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-427 (line)]] | wt | 8.34 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.103× (z -9.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 5.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0608× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0790× (z -11.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.108× (z -8.7) |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC20-OT1]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UBE2CP5]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[SLC23A3]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[POLN]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.67 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CCNP]] | +0.67 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[FLJ46284]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[TNXB]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[APRG1]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[SSX2IP]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ZDHHC21]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SCCPDH]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[IPO8]] | -0.54 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[MDM1]] | -0.54 | -0.37 / -0.49 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | MUC20 activity raises SMBD1P's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.30× lower at baseline in the lines without MUC20 | 0.005 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises SMBD1P's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without MROH3P | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[MROH3P]] | B | MROH3P activity strengthens SMBD1P's drug response | lines that do not express MROH3P (26) vs lines expressing it (19) | the lines without MROH3P respond 0.62× as strongly (z diff +1.43); strongest at Homoharringtonine 5 µM: 0.70x vs 0.42x (z diff +3.2) | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; target measured in part of the lines; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AADAT]] | C | SMBD1P activity lowers AADAT's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.63× higher at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |
| [[LINC00672]] | C | SMBD1P activity raises LINC00672's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SLC22A20P]] | C | SMBD1P activity raises SLC22A20P's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |
| [[IPO8]] | C | SMBD1P activity lowers IPO8's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.01× higher at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |
| [[AVIL]] | C | SMBD1P activity raises AVIL's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without SMBD1P | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |
| [[MDM1]] | C | SMBD1P activity lowers MDM1's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 1.82× higher at baseline in the lines without SMBD1P | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |
| [[SLC22A14]] | C | SMBD1P activity raises SLC22A14's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without SMBD1P | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent |
| [[SLC22A13]] | C | SMBD1P activity raises SLC22A13's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without SMBD1P | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.3, -20.4); signed map (10.6, 8.7). **Vector** length 95.3, 23.9% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +1.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.4 | -7.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.2 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | somatomedin B domain containing 1, pseudogene |
| Locus type | pseudogene |
| Location | 3q29 — chr3:195,701,618-195,711,643 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53806) · Entrez [111674481](https://www.ncbi.nlm.nih.gov/gene/111674481) · Ensembl [ENSG00000283426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283426)

## Data

Gene col 16026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16026); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16026]; `tensor/DDL_lfc|DDL_z.npy` [16026]; `embed/gene_vectors.npy` [16026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16026 or target_col == 16026). Every well: [[SMBD1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMBD1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
