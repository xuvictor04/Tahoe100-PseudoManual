---
symbol: "PCGF3-AS1"
type: "gene"
col: 14622
ensembl_id: "ENSG00000249592"
name: "PCGF3 antisense RNA 1"
location: "4p16.3"
module: 49
arm: "+"
pooled_cpm: 75.84
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PCGF3-AS1

*PCGF3 antisense RNA 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +10.1, q 5e-21, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.480× (z -9.3, q 1e-17, down in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.752× (z -4.6, q 3e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC33A1]] (+0.79, fdr 7e-06), [[TMED7-TICAM2]] (+0.74, fdr 7e-06), [[GOSR2]] (+0.68, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CADPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.1 | 5e-21 | 45/49 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +7.2 | 2e-10 | 35/48 (A-172, SW 900, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.029 | 26/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.31 | 18/48 (LoVo, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.480×** | -9.3 | 1e-17 | 35/48 (A549, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.525×** | -8.2 | 1e-13 | 35/43 (H4, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.546×** | -7.6 | 4e-12 | 38/47 (LoVo, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.636×** | -7.5 | 1e-11 | 29/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.577×** | -7.2 | 6e-11 | 34/49 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.661×** | -5.0 | 4e-05 | 29/45 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.683×** | -5.0 | 4e-05 | 28/48 (A549, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.752×** | -4.6 | 3e-04 | 30/48 (A-172, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.709×** | -4.5 | 4e-04 | 29/48 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -3.9 | 0.006 | 26/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -3.8 | 0.009 | 27/48 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.638×** | -3.1 | 0.094 | 21/47 (SHP-77, SW1417, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.9 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.49× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A549 (line)]] | wt | 53.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.6) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A498 (line)]] | wt | 49.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.293× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 185 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +9.6) ⚠ cell-cycle shift, explains ~77% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -11.5) ⚠ cell-cycle shift, explains ~77% of this change |
| [[A-427 (line)]] | wt | 57.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 104 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +10.1) ⚠ cell-cycle shift, explains ~77% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HS-578T (line)]] | alt | 57.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[HT-29 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.329× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 47.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.9) ⚠ cell-cycle shift, explains ~82% of this change |
| [[Panc 03.27 (line)]] | alt | 54.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 48.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.355× (z -10.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 62.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.21× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[AsPC-1 (line)]] | alt | 52.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[C32 (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.272× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 80.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[H4 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[Hs 766T (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 87.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 66.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 53.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.56× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.3) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SW48 (line)]] | wt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC33A1]] | +0.79 | +0.76 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[TMED7-TICAM2]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[TMEM165]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CAPN10-DT]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ALG11]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PLPP5]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[OSTC]] | +0.64 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.64 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[LMAN2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SPCS2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADPS2]] | B | CADPS2 activity raises PCGF3-AS1's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without CADPS2 | 0.031 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.1, -28.5); signed map (-45.9, 11.0). **Vector** length 126, 39.8% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.2 | -9.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -4.4 | -7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Busulfan (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | PCGF3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p16.3 — chr4:760,202-781,866 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56108) · Entrez [100129917](https://www.ncbi.nlm.nih.gov/gene/100129917) · Ensembl [ENSG00000249592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249592)

## Data

Gene col 14622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14622); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14622]; `tensor/DDL_lfc|DDL_z.npy` [14622]; `embed/gene_vectors.npy` [14622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14622 or target_col == 14622). Every well: [[PCGF3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCGF3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
