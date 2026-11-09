---
symbol: "FLNC"
type: "gene"
col: 4899
ensembl_id: "ENSG00000128591"
name: "filamin C"
location: "7q32.1"
module: 111
arm: "+"
pooled_cpm: 21.1
n_lines_expressing: 23
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# FLNC

*filamin C* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.78× (z +18.3, q 0e+00, up in 20 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.652× (z -6.3, q 2e-07, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTAN1]] (+0.57, fdr 3e-05), [[ADAMTS1]] (+0.57, fdr 1e-05), [[DBN1]] (+0.56, fdr 5e-05); moves opposite to [[NDUFC1]] (-0.56, fdr 1e-04), [[SELENOH]] (-0.55, fdr 6e-05), [[LEMD3]] (-0.54, fdr 8e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CREB5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CNN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.78×** | +18.3 | 0e+00 | 20/21 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +13.9 | 1e-41 | 12/16 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +12.3 | 3e-32 | 15/20 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +11.0 | 4e-26 | 8/17 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +10.2 | 1e-22 | 13/21 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +8.7 | 2e-16 | 14/21 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +6.6 | 4e-09 | 10/21 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +6.0 | 1e-07 | 15/21 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.74×** | +5.8 | 5e-07 | 10/21 (A-427, SW 900, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 8e-07 | 14/21 (A498, A-172, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.46×** | +5.6 | 1e-06 | 11/21 (SK-MEL-2, SW 900, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.5 | 2e-06 | 4/21 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +5.2 | 8e-06 | 11/21 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.8 | 6e-05 | 6/21 (SK-MEL-2, LS 180, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +4.8 | 7e-05 | 8/21 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 2e-04 | 9/21 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.7 | 0.005 | 6/21 (SW 900, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.93×** | +3.6 | 0.008 | 5/20 (NCI-H1792, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.008 | 3/21 (CFPAC-1, CHP-212, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -6.3 | 2e-07 | 18/21 (Hs 766T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -4.5 | 0.002 | 4/21 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.657×** | -4.4 | 0.002 | 13/21 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.011 | 12/20 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.033 | 14/21 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.732× | -3.2 | 0.11 | 11/21 (J82, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 73.6 | 7 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 20.5× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -14.2) |
| [[HS-578T (line)]] | alt | 72.9 | 2 | 2 | [[Auranofin (drug)]] 5 µM 4.87× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 5.28 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 160× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 23.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +14.4) | — |
| [[A498 (line)]] | wt | 114 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.9) | — |
| [[J82 (line)]] | alt | 37.1 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 7.00× (z +12.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.4) |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 25.1 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -15.6) |
| [[PANC-1 (line)]] | alt | 5.54 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.46× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 5.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 31.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.22× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 18.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 15.3× (z +12.3) | — |
| [[A-172 (line)]] | wt | 15.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.87× (z +10.3) | — |
| [[A-427 (line)]] | wt | 31.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.49× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.5) |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0819× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 146 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 80.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.65× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 8.24 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.5× (z +9.1) | — |
| [[A549 (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTAN1]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 | pathway: Cell-Cell communication |
| [[ADAMTS1]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DBN1]] | +0.56 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[OCRL]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CNN3]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 | STRING 437 |
| [[STIP1]] | +0.54 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[PRELID3B]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SLC35F6]] | +0.53 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[ARHGAP23]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PALLD]] | +0.53 | +0.49 / +0.46 | both halves | 2e-05 | STRING 445 |
| [[ADAMTSL5]] | +0.53 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[DST]] | +0.52 | +0.40 / +0.59 | both halves | 5e-05 | pathway: Cell junction organization |

## Genes that move opposite

*43 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFC1]] | -0.56 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[SELENOH]] | -0.55 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[LEMD3]] | -0.54 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[NDUFAF6]] | -0.54 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[HOXA5]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[MBTD1]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SNHG9]] | -0.52 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[TAF5]] | -0.52 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[NUP54]] | -0.52 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[SMIM27]] | -0.51 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[FAM76B]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GPX1]] | -0.51 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB5]] | B | CREB5 activity lowers FLNC's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.12× higher at baseline in the lines without CREB5 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[ARHGAP23]] | B | ARHGAP23 activity raises FLNC's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without ARHGAP23 | 0.091 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNN3]] | B | FLNC activity raises CNN3's level | lines that do not express FLNC (27) vs lines expressing it (23) | 1.91× lower at baseline in the lines without FLNC | 0.070 | ⚠ within organs, on part of the lines; also absent: EDNRA, MOXD1, ARMCX1 |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.1, 35.8); signed map (-4.5, 33.2). **Vector** length 69.5, 19.2% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +1.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.8 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.5 | -6.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | filamin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,830,406-128,859,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ABP-280, ABPL; previously FLN2 |
| Gene groups (HGNC) | Filamin family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Cell-extracellular matrix interactions; Cell junction organization; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14315](https://www.uniprot.org/uniprotkb/Q14315) (Filamin-C):

> Muscle-specific filamin, which plays a central role in sarcomere assembly and organization. Critical for normal myogenesis, it probably functions as a large actin-cross-linking protein with structural functions at the Z lines in muscle cells. May be involved in reorganizing the actin cytoskeleton in response to signaling events (By similarity).

**Summary**, from NCBI Gene [2318](https://www.ncbi.nlm.nih.gov/gene/2318):

> This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membrane glycoprotein-binding domain. Mutations in this gene are a cause of cardiopathy. Two transcript …

**Accessions** — [HGNC:3756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3756) · Entrez [2318](https://www.ncbi.nlm.nih.gov/gene/2318) · UniProt [Q14315](https://www.uniprot.org/uniprotkb/Q14315) · Ensembl [ENSG00000128591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128591)

## Data

Gene col 4899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4899); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4899]; `tensor/DDL_lfc|DDL_z.npy` [4899]; `embed/gene_vectors.npy` [4899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4899 or target_col == 4899). Every well: [[FLNC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLNC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
