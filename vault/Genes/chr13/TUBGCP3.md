---
symbol: "TUBGCP3"
type: "gene"
col: 4720
ensembl_id: "ENSG00000126216"
name: "tubulin gamma complex component 3"
location: "13q34"
module: 6
arm: "+"
pooled_cpm: 58.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TUBGCP3

*tubulin gamma complex component 3* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.68× (z +4.5, q 0.004, up in 22 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.464× (z -17.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP2]] (+0.83, fdr 7e-06), [[NCAPD3]] (+0.79, fdr 7e-06), [[CSE1L]] (+0.77, fdr 7e-06); moves opposite to [[CD63]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.5 | 0.004 | 22/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.014 | 24/48 (hTERT-HPNE, NCI-H2030, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.030 | 20/48 (A498, SW1417, …) | all doses, flat |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.6 | 0.042 | 17/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.14 | 12/48 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | 1.45× | +3.2 | 0.14 | 14/48 (PANC-1, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.464×** | -17.7 | 0e+00 | 48/48 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -15.4 | 0e+00 | 39/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -8.5 | 5e-15 | 34/47 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -8.2 | 5e-14 | 36/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.617×** | -7.9 | 4e-13 | 34/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -7.3 | 2e-11 | 32/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -7.0 | 2e-10 | 30/48 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -6.8 | 7e-10 | 32/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.676×** | -6.4 | 1e-08 | 32/48 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -6.2 | 3e-08 | 33/49 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -5.8 | 3e-07 | 31/48 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -5.3 | 6e-06 | 29/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -5.1 | 2e-05 | 21/48 (HEC-1-A, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.7 | 1e-04 | 26/48 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.751×** | -4.6 | 1e-04 | 25/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.753×** | -4.6 | 2e-04 | 28/48 (A-427, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 95.6 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -15.7) |
| [[HT-29 (line)]] | alt | 77.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 50.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.9) |
| [[COLO 205 (line)]] | alt | 148 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 62.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.0) |
| [[SNU-1 (line)]] | wt | 74.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 50.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.6) |
| [[Hs 766T (line)]] | wt | 52.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.3) |
| [[LoVo (line)]] | wt | 49.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -22.2) |
| [[PANC-1 (line)]] | alt | 52.2 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -19.5) |
| [[SW480 (line)]] | alt | 136 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -14.3) |
| [[A498 (line)]] | wt | 37.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -19.1) |
| [[C32 (line)]] | wt | 52.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.5) |
| [[HOP62 (line)]] | alt | 40.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.6) |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -12.4) |
| [[SHP-77 (line)]] | alt | 157 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -13.8) |
| [[SW 900 (line)]] | alt | 40.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.6) |
| [[HCT15 (line)]] | alt | 79.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -10.7) |
| [[J82 (line)]] | alt | 96.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 49.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -13.9) |
| [[LS 180 (line)]] | wt | 70.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 69.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.3) |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.9) |
| [[A-427 (line)]] | wt | 76.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.541× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 65.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -14.8) |
| [[RKO (line)]] | wt | 60.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.4) |
| [[SW1417 (line)]] | alt | 41.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.1) |
| [[SW48 (line)]] | wt | 70.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP2]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 741 |
| [[NCAPD3]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.77 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[CEP78]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Centrosome maturation |
| [[NUP155]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[HNRNPR]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TIMELESS]] | +0.72 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[FANCG]] | +0.72 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[HAUS1]] | +0.72 | +0.75 / +0.64 | both halves | 7e-06 | pathway: Centrosome maturation |
| [[CCDC150]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD63]] | -0.62 | -0.50 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TUBGCP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises TUBGCP3's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without DSCC1 | 0.069 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.2, -42.7); signed map (-34.2, -42.8). **Vector** length 116, 34.0% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.54 to 65); *DNA strand elongation* (reactome, mean cos +0.56 to 28); *DNA Replication* (reactome, mean cos +0.54 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +4.0 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.8 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -17.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -8.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.6 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -15.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma complex component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:112,485,011-112,588,205 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCP3, Spc98p, SPBC98 |
| Gene groups (HGNC) | Tubulin gamma complex component family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CW5](https://www.uniprot.org/uniprotkb/Q96CW5) (Gamma-tubulin complex component 3):

> Component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [10426](https://www.ncbi.nlm.nih.gov/gene/10426):

> Enables gamma-tubulin binding activity. Predicted to be involved in meiotic cell cycle; microtubule cytoskeleton organization; and mitotic cell cycle. Located in cytoplasm and microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18598) · Entrez [10426](https://www.ncbi.nlm.nih.gov/gene/10426) · UniProt [Q96CW5](https://www.uniprot.org/uniprotkb/Q96CW5) · Ensembl [ENSG00000126216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126216)

## Data

Gene col 4720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4720); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4720]; `tensor/DDL_lfc|DDL_z.npy` [4720]; `embed/gene_vectors.npy` [4720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4720 or target_col == 4720). Every well: [[TUBGCP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBGCP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
