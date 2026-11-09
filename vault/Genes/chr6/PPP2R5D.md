---
symbol: "PPP2R5D"
type: "gene"
col: 3387
ensembl_id: "ENSG00000112640"
name: "protein phosphatase 2 regulatory subunit B'delta"
location: "6p21.1"
module: 22
arm: "+"
pooled_cpm: 33.03
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PPP2R5D

*protein phosphatase 2 regulatory subunit B'delta* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.00× (z +13.4, q 5e-38, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.744× (z -5.7, q 8e-06, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.136×, LOX-IMVI 0.119×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.409×, SK-MEL-2 0.267×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.283×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.186×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMG20B]] (+0.70, fdr 7e-06), [[CRAT]] (+0.69, fdr 7e-06), [[SETD3]] (+0.68, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +13.4 | 5e-38 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +10.9 | 2e-25 | 41/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +10.7 | 1e-24 | 37/48 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +10.6 | 4e-24 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.64×** | +9.5 | 2e-19 | 30/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.54×** | +8.0 | 1e-13 | 24/38 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.40×** | +6.5 | 6e-09 | 30/46 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 3e-06 | 27/47 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.1 | 2e-05 | 26/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.7 | 2e-04 | 21/48 (CFPAC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +4.3 | 1e-03 | 21/48 (MIA PaCa-2, LS 180, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.0 | 0.004 | 20/47 (SW48, LS 180, …) | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.035 | 6/47 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.038 | 13/48 (HS-578T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.20×** | +3.3 | 0.041 | 16/42 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.071 | 11/48 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.136×, LOX-IMVI 0.119×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.409×, SK-MEL-2 0.267×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.283×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.744×** | -5.7 | 8e-06 | 24/48 (Panc 03.27, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.754×** | -5.4 | 2e-05 | 26/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.8 | 0.027 | 18/48 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.827×** | -3.6 | 0.040 | 11/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.849× | -3.0 | 0.27 | 6/48 (HOP62, LoVo, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 38.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +10.2) | — |
| [[KATO III (line)]] | alt | 31.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +10.2) | — |
| [[SW480 (line)]] | alt | 28.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.63× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Lonafarnib (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 37.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.283× (z -15.8) |
| [[A549 (line)]] | wt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 27.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.186× (z -10.3) |
| [[HOP62 (line)]] | alt | 39.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +8.7) | — |
| [[LoVo (line)]] | wt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.119× (z -10.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 58.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -9.4) |
| [[RKO (line)]] | wt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -8.6) |
| [[SW1417 (line)]] | alt | 34.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +8.6) | — |
| [[A-172 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMG20B]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CRAT]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SETD3]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CKAP5]] | +0.66 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[REEP4]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[HNRNPUL2]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[APPL1]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SPAG5]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TAF6]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 | same gene group |
| [[INCENP]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[KIF20A]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[GTF3C1]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises PPP2R5D's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without PIMREG | 0.016 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PPP2R5D's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NEURL1B]] | B | NEURL1B activity raises PPP2R5D's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without NEURL1B | 0.088 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PBK]] | C | PBK activity raises PPP2R5D's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without PBK | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises PPP2R5D's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.5, -53.4); signed map (-48.6, -12.6). **Vector** length 101, 23.6% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | +4.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.4 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +13.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +10.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +1.7 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +1.7 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B'delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,984,553-43,012,342 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B56D, B56delta |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; Armadillo like helical domain containing |
| Reactome | 91 pathways, smallest: PP2A-mediated dephosphorylation of key metabolic factors; Regulation of glycolysis by fructose 2,6-bisphosphate metabolism; ERKs are inactivated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14738](https://www.uniprot.org/uniprotkb/Q14738) (Serine/threonine-protein phosphatase 2A 56 kDa regulatory subunit delta isoform):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment.

**Summary**, from NCBI Gene [5528](https://www.ncbi.nlm.nih.gov/gene/5528):

> The product of this gene belongs to the phosphatase 2A regulatory subunit B family. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9312) · Entrez [5528](https://www.ncbi.nlm.nih.gov/gene/5528) · UniProt [Q14738](https://www.uniprot.org/uniprotkb/Q14738) · Ensembl [ENSG00000112640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112640)

## Data

Gene col 3387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3387); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3387]; `tensor/DDL_lfc|DDL_z.npy` [3387]; `embed/gene_vectors.npy` [3387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3387 or target_col == 3387). Every well: [[PPP2R5D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R5D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
