---
symbol: "RUSF1"
type: "gene"
col: 6442
ensembl_id: "ENSG00000140688"
name: "RUS family member 1"
location: "16p11.2"
module: 49
arm: "+"
pooled_cpm: 21.49
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RUSF1

*RUS family member 1* — 16p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (22 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.359× (z -18.2, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.423× (z -15.3, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL1]] (+0.74, fdr 7e-06), [[GOLGA5]] (+0.73, fdr 7e-06), [[SLC33A1]] (+0.72, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.359×** | -18.2 | 0e+00 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.370×** | -17.7 | 0e+00 | 46/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.423×** | -15.3 | 0e+00 | 41/48 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.463×** | -13.7 | 1e-40 | 44/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.581×** | -13.7 | 2e-40 | 39/47 (A549, NCI-H2347, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -9.5 | 1e-19 | 34/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.595×** | -8.9 | 6e-17 | 31/45 (SHP-77, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.615×** | -8.7 | 3e-16 | 34/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.722×** | -8.2 | 2e-14 | 31/47 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.621×** | -8.2 | 2e-14 | 32/47 (H4, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.657×** | -7.5 | 4e-12 | 30/48 (KATO III, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -6.8 | 5e-10 | 27/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.683×** | -6.8 | 5e-10 | 30/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -6.2 | 3e-08 | 30/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -5.8 | 2e-07 | 30/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.711×** | -5.7 | 4e-07 | 21/47 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.734×** | -5.2 | 6e-06 | 22/48 (SNU-423, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.4 | 3e-04 | 15/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.016 | 8/48 (PANC-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.731×** | -2.9 | 0.064 | 16/46 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.852× | -2.8 | 0.077 | 9/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.894× | -2.8 | 0.087 | 9/48 (LS 180, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.5 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0859× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -11.0) |
| [[H4 (line)]] | wt | 37.5 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.118× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 25.7 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.403× (z -8.9) |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 5 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.187× (z -10.3) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.176× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.284× (z -10.3) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.295× (z -8.7) |
| [[A-172 (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.270× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[KATO III (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 20.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -10.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.103× (z -11.2) |
| [[Hs 766T (line)]] | wt | 36.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.339× (z -8.6) |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -14.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0845× (z -16.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL1]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GOLGA5]] | +0.73 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[COPG1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[COG3]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[DERL2]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ALG5]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[FAM114A2]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[OSTC]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ZNF550]] | +0.67 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[AAAS]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[MED8]] | +0.66 | +0.75 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RUSF1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, -37.4); signed map (-54.5, 12.5). **Vector** length 73.2, 14.2% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.51 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.51 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +2.7 | -3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.7 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.1 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +0.8 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.3 | +0.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.3 | -18.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.1 | -13.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -15.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -17.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -5.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RUS family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,489,471-31,509,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13868; previously C16orf58 |
| Matched by | ensembl_id |

UniProt [Q96GQ5](https://www.uniprot.org/uniprotkb/Q96GQ5) carries no function annotation.

**Summary**, from NCBI Gene [64755](https://www.ncbi.nlm.nih.gov/gene/64755):

> This gene encodes a putative transmembrane protein containing a conserved DUF647 domain that may be involved in protein-protein interaction. The encoded protein is related to a plant protein that participates in ultraviolet B light-sensing during root morphogenesis. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:25848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25848) · Entrez [64755](https://www.ncbi.nlm.nih.gov/gene/64755) · UniProt [Q96GQ5](https://www.uniprot.org/uniprotkb/Q96GQ5) · Ensembl [ENSG00000140688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140688)

## Data

Gene col 6442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6442); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6442]; `tensor/DDL_lfc|DDL_z.npy` [6442]; `embed/gene_vectors.npy` [6442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6442 or target_col == 6442). Every well: [[RUSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
