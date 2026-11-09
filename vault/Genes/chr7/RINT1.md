---
symbol: "RINT1"
type: "gene"
col: 5670
ensembl_id: "ENSG00000135249"
name: "RAD50 interactor 1"
location: "7q22.3"
module: 49
arm: "+"
pooled_cpm: 61.26
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RINT1

*RAD50 interactor 1* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.41× (z +4.6, q 0.003, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.505× (z -9.6, q 5e-19, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Busulfan (drug)]] 0.05 µM: 0.692× (z -5.2, q 3e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG6]] (+0.78, fdr 7e-06), [[RARS2]] (+0.75, fdr 7e-06), [[TMEM39A]] (+0.75, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 0.003 | 30/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.006 | 31/48 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.015 | 26/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.094 | 22/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.18 | 20/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.18 | 21/48 (Panc 03.27, SW480, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.505×** | -9.6 | 5e-19 | 43/49 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -8.2 | 6e-14 | 35/45 (HepG2/C3A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -8.2 | 6e-14 | 30/41 (C32, H4, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.692×** | -5.2 | 3e-05 | 34/48 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -5.1 | 4e-05 | 25/48 (CHP-212, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.715×** | -4.7 | 2e-04 | 30/48 (A498, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -4.5 | 5e-04 | 28/47 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.730×** | -4.4 | 7e-04 | 31/48 (A498, SW 1088, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.3 | 0.001 | 27/48 (A498, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.741×** | -4.2 | 0.002 | 28/48 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -4.2 | 0.002 | 25/48 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Thymol (drug)]] 5 µM |  | **0.805×** | -4.1 | 0.002 | 27/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.750×** | -4.0 | 0.002 | 26/48 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.757×** | -3.9 | 0.004 | 26/49 (SW 900, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.765×** | -3.8 | 0.006 | 25/49 (LS 180, SW 900, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.774×** | -3.6 | 0.012 | 24/49 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.791×** | -3.3 | 0.034 | 22/49 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.795×** | -3.2 | 0.041 | 21/48 (KATO III, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.845× | -3.2 | 0.041 | 20/48 (A498, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 132 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.528× (z -9.2) |
| [[A-172 (line)]] | wt | 46.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.9) |
| [[H4 (line)]] | wt | 104 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0373× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 82.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 45.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0695× (z -20.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 44.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -12.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -10.4) |
| [[HCT15 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -11.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 73.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.8) |
| [[LoVo (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 67.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -8.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -17.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -14.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 82.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0704× (z -9.6) ⚠ toxic |
| [[SW480 (line)]] | alt | 68.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG6]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 639 |
| [[RARS2]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[AARSD1]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[OSTC]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[RARS1]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SRP54]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[GPR107]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[SSR2]] | +0.71 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[DHDDS]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CRLS1]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RINT1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises RINT1's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without SNHG18 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, -33.1); signed map (-48.7, 9.6). **Vector** length 117, 37.0% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.52 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.52 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | -0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +3.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | RAD50 interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:105,532,169-105,567,677 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11785, RINT-1 |
| Gene groups (HGNC) | NRZ tethering complex |
| Reactome | 5 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUQ1](https://www.uniprot.org/uniprotkb/Q6NUQ1) (RAD50-interacting protein 1):

> Involved in regulation of membrane traffic between the Golgi and the endoplasmic reticulum (ER); the function is proposed to depend on its association in the NRZ complex which is believed to play a role in SNARE assembly at the ER. May play a role in cell cycle checkpoint control. Essential for telomere length control.

**Summary**, from NCBI Gene [60561](https://www.ncbi.nlm.nih.gov/gene/60561):

> This gene encodes a protein first identified for its ability to interact with the RAD50 double strand break repair protein, with the resulting interaction implicated in the regulation of cell cycle progression and telomere length. The encoded protein may also play a role in trafficking of cellular cargo from the endosome to the trans-Golgi network. Mutations in this gene may be associated with breast cancer in human patients. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:21876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21876) · Entrez [60561](https://www.ncbi.nlm.nih.gov/gene/60561) · UniProt [Q6NUQ1](https://www.uniprot.org/uniprotkb/Q6NUQ1) · Ensembl [ENSG00000135249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135249)

## Data

Gene col 5670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5670); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5670]; `tensor/DDL_lfc|DDL_z.npy` [5670]; `embed/gene_vectors.npy` [5670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5670 or target_col == 5670). Every well: [[RINT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RINT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
