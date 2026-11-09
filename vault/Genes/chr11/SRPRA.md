---
symbol: "SRPRA"
type: "gene"
col: 11345
ensembl_id: "ENSG00000182934"
name: "SRP receptor subunit alpha"
location: "11q24.2"
module: 42
arm: "+"
pooled_cpm: 65.17
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SRPRA

*SRP receptor subunit alpha* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +8.8, q 1e-15, up in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.55× (z +6.2, q 8e-08, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 0.731× (z -4.5, q 0.004, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Furosemide (drug)]] 0.05 µM in 1 line (NCI-H661 0.0876×); [[Panobinostat (drug)]] 5 µM in 1 line (A498 0.461×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (H4 0.0881×; ⚠ toxic); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.113×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.140×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM214]] (+0.77, fdr 7e-06), [[SSR1]] (+0.75, fdr 7e-06), [[SLC39A7]] (+0.74, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[HM13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.8 | 1e-15 | 29/41 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.60×** | +6.7 | 5e-09 | 40/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.58×** | +6.5 | 1e-08 | 30/49 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +6.2 | 8e-08 | 36/48 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +5.0 | 6e-05 | 36/48 (PANC-1, SNU-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +4.5 | 7e-04 | 29/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +4.1 | 0.003 | 23/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.004 | 28/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.33×** | +4.0 | 0.004 | 27/48 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.35×** | +4.0 | 0.004 | 25/45 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.014 | 21/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.19× | +3.6 | 0.018 | 17/49 (COLO 205, PANC-1, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.1 | 0.076 | 18/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.089 | 10/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.097 | 14/48 (SW1417, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11345.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Furosemide (drug)]] 0.05 µM in 1 line (NCI-H661 0.0876×); [[Panobinostat (drug)]] 5 µM in 1 line (A498 0.461×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (H4 0.0881×; ⚠ toxic); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.113×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.140×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **0.731×** | -4.5 | 0.004 | 32/48 (AsPC-1, KATO III, …) | two highest doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.775×** | -3.7 | 0.071 | 25/48 (J82, NCI-H23, …) | two highest doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.779× | -3.4 | 0.11 | 25/48 (HepG2/C3A, A498, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.854× | -3.2 | 0.19 | 12/48 (HCT15, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 70.8 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 28.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.74× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 62.3 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.37× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +15.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A-427 (line)]] | wt | 39.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A498 (line)]] | wt | 67.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.461× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.140× (z -8.7) |
| [[H4 (line)]] | wt | 84.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0881× (z -8.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 44.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.284× (z -8.7) |
| [[HOP62 (line)]] | alt | 59.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 49.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H596 (line)]] | alt | 59.4 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 1.99× (z +12.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0876× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.113× (z -8.8) |
| [[AN3 CA (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 170 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 66.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM214]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SSR1]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 752 |
| [[SLC39A7]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SEC61A1]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 957 |
| [[SURF4]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[DAP]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GOLGA3]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TMED2]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[LRRC59]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[COPG1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 | STRING 460 |
| [[HDLBP]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[USO1]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HM13]] | C | SRPRA's natural level strengthens HM13's drug response | SRPRA's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.12; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[B4GALT5]] | C | SRPRA's natural level weakens B4GALT5's drug response | SRPRA's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.13; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -30.1); signed map (-55.6, 8.7). **Vector** length 106, 29.7% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.52 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.50 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.8 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Isocorydine (drug)]] 5 µM |  | +1.9 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SRP receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,262,938-126,269,144 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRP-alpha, Sralpha, SR-alpha; previously SRPR |
| Gene groups (HGNC) | Signal recognition particle GTPases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 7 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [P08240](https://www.uniprot.org/uniprotkb/P08240) (Signal recognition particle receptor subunit alpha):

> Component of the signal recognition particle (SRP) complex receptor (SR). Ensures, in conjunction with the SRP complex, the correct targeting of the nascent secretory proteins to the endoplasmic reticulum membrane system. Forms a guanosine 5'-triphosphate (GTP)-dependent complex with the SRP subunit SRP54. SRP receptor compaction and GTPase rearrangement drive SRP-mediated cotranslational protein translocation into the ER.

**Summary**, from NCBI Gene [6734](https://www.ncbi.nlm.nih.gov/gene/6734):

> The gene encodes a subunit of the endoplasmic reticulum signal recognition particle receptor that, in conjunction with the signal recognition particle, is involved in the targeting and translocation of signal sequence tagged secretory and membrane proteins across the endoplasmic reticulum. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:11307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11307) · Entrez [6734](https://www.ncbi.nlm.nih.gov/gene/6734) · UniProt [P08240](https://www.uniprot.org/uniprotkb/P08240) · Ensembl [ENSG00000182934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182934)

## Data

Gene col 11345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11345); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11345]; `tensor/DDL_lfc|DDL_z.npy` [11345]; `embed/gene_vectors.npy` [11345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11345 or target_col == 11345). Every well: [[SRPRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRPRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
