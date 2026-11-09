---
symbol: "RSPH9"
type: "gene"
col: 10254
ensembl_id: "ENSG00000172426"
name: "radial spoke head component 9"
location: "6p21.1"
module: 37
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# RSPH9

*radial spoke head component 9* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.50× (z +27.7, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.698× (z -3.8, q 0.083, down in 10 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0302×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (PANC-1 0.105×; ⚠ toxic; transcription drop); [[Naproxen (drug)]] 5 µM in 1 line (NCI-H2347 0.0772×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H2030 0.128×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.0842×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM184B]] (+0.71, fdr 7e-06), [[PLA2G12B]] (+0.71, fdr 7e-06), [[SPATA1]] (+0.71, fdr 7e-06); moves opposite to [[THEM6]] (-0.60, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.50×** | +27.7 | 0e+00 | 32/34 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.99×** | +16.2 | 0e+00 | 27/34 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.06×** | +11.3 | 3e-27 | 8/18 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +9.2 | 4e-18 | 18/31 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.48×** | +9.2 | 4e-18 | 15/31 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +8.9 | 4e-17 | 19/34 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +8.8 | 2e-16 | 1/7 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.1 | 5e-14 | 11/43 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.2 | 1e-05 | 3/15 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 14/41 (SW480, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +4.4 | 6e-04 | 9/46 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.3 | 7e-04 | 1/17 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 6/43 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +4.0 | 0.003 | 12/44 (SW480, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.010 | 4/47 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.012 | 6/38 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.063 | 5/40 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.072 | 6/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0302×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (PANC-1 0.105×; ⚠ toxic; transcription drop); [[Naproxen (drug)]] 5 µM in 1 line (NCI-H2347 0.0772×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H2030 0.128×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.0842×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -3.8 | 0.083 | 10/44 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Allantoin (drug)]] 5 µM |  | 0.800× | -3.3 | 0.18 | 8/43 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.722× | -3.3 | 0.18 | 10/37 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Elagolix sodium (drug)]] 5 µM |  | 0.816× | -3.1 | 0.31 | 6/43 (hTERT-HPNE, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.82 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +10.8) | [[Belumosudil (drug)]] 5 µM 0.0842× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0302× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 6.97 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.2) | [[Hydroxyurea (drug)]] 0.05 µM 0.128× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 3.21 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +10.9) | [[Naproxen (drug)]] 5 µM 0.0772× (z -9.6) |
| [[PANC-1 (line)]] | alt | 4.83 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.0× (z +9.4) | — |
| [[A498 (line)]] | wt | 1.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +11.6) | — |
| [[C32 (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 5.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 3.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 7.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.149× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 3.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.27× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +9.3) | — |
| [[SW480 (line)]] | alt | 2.16 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0732× (z -8.7) |
| [[A-427 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM184B]] | +0.71 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.71 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LINC03016]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TEX29]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[COLEC11]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.60 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RSPH9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.2, -17.4); signed map (12.8, 7.2). **Vector** length 64.6, 9.72% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +27.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | radial spoke head component 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,645,036-43,672,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30845, CILD12; previously MRPS18AL1, C6orf206 |
| Gene groups (HGNC) | Axonemal radial spoke subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1X1](https://www.uniprot.org/uniprotkb/Q9H1X1) (Radial spoke head protein 9 homolog):

> Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia. Essential for both the radial spoke head assembly and the central pair microtubule stability in ependymal motile cilia (By similarity). Required for motility of olfactory and neural cilia and for the structural integrity of ciliary axonemes in both 9+0 and 9+2 motile cilia (By similarity).

**Summary**, from NCBI Gene [221421](https://www.ncbi.nlm.nih.gov/gene/221421):

> This gene encodes a protein thought to be a component of the radial spoke head in motile cilia and flagella. Mutations in this gene are associated with primary ciliary dyskinesia 12. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:21057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21057) · Entrez [221421](https://www.ncbi.nlm.nih.gov/gene/221421) · UniProt [Q9H1X1](https://www.uniprot.org/uniprotkb/Q9H1X1) · Ensembl [ENSG00000172426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172426)

## Data

Gene col 10254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10254); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10254]; `tensor/DDL_lfc|DDL_z.npy` [10254]; `embed/gene_vectors.npy` [10254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10254 or target_col == 10254). Every well: [[RSPH9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSPH9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
