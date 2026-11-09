---
symbol: "UBE2D1"
type: "gene"
col: 1017
ensembl_id: "ENSG00000072401"
name: "ubiquitin conjugating enzyme E2 D1"
location: "10q21.1"
module: 93
arm: "+"
pooled_cpm: 59.43
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# UBE2D1

*ubiquitin conjugating enzyme E2 D1* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +14.5, q 1e-44, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.721× (z -5.0, q 3e-04, down in 24 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (SW48 0.270×, AsPC-1 0.334×, NCI-H2347 0.428×; ⚠ unreliable plate only); [[Docetaxel (drug)]] 0.05 µM in 1 line (HS-578T 0.191×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (CHP-212 0.0895×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABI1]] (+0.59, fdr 1e-05), [[USP53]] (+0.58, fdr 1e-05), [[SUGT1]] (+0.57, fdr 3e-05); moves opposite to [[CPSF7]] (-0.50, fdr 2e-05), [[HMGXB3]] (-0.47, fdr 1e-04), [[SETD1A]] (-0.46, fdr 7e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +14.5 | 1e-44 | 38/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.6 | 5e-24 | 34/49 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +9.2 | 5e-18 | 41/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +8.5 | 4e-15 | 39/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +7.6 | 5e-12 | 37/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +7.4 | 9e-12 | 34/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +7.0 | 2e-10 | 38/48 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +6.4 | 1e-08 | 33/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +6.2 | 4e-08 | 32/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +6.1 | 7e-08 | 32/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +5.7 | 7e-07 | 35/48 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 29/48 (J82, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.3 | 4e-06 | 25/49 (LS 180, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 1e-04 | 27/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +4.5 | 2e-04 | 27/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +4.3 | 5e-04 | 26/47 (HT-29, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (SW48 0.270×, AsPC-1 0.334×, NCI-H2347 0.428×; ⚠ unreliable plate only); [[Docetaxel (drug)]] 0.05 µM in 1 line (HS-578T 0.191×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (CHP-212 0.0895×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -5.0 | 3e-04 | 24/48 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.648× | -3.4 | 0.16 | 20/48 (LoVo, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.3 | 0.16 | 17/48 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.818× | -3.1 | 0.30 | 18/48 (NCI-H23, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 44.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.0) | — |
| [[SW480 (line)]] | alt | 59.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.2) | — |
| [[A498 (line)]] | wt | 39.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 35.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.27× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 51.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 71.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -9.0) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 33.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +16.1) | — |
| [[KATO III (line)]] | alt | 36.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.15× (z +11.1) | — |
| [[LoVo (line)]] | wt | 58.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.6) | — |
| [[RKO (line)]] | wt | 85.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.0) | — |
| [[A-172 (line)]] | wt | 45.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.8) | — |
| [[A-427 (line)]] | wt | 52.1 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +10.3) | — |
| [[C32 (line)]] | wt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +13.7) | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0895× (z -9.1) |
| [[HS-578T (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.191× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.6) | — |
| [[J82 (line)]] | alt | 33.9 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 61.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 96.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 73.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.428× (z -8.8) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.126× (z -8.8) ⚠ toxic |
| [[SW 900 (line)]] | alt | 88.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.9) | — |
| [[SW48 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -9.4) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 177 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI1]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[USP53]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SUGT1]] | +0.57 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[CHCHD7]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 | pathway: Protein localization |
| [[LGMN]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 | pathway: Toll-like Receptor Cascades |
| [[PPP4R1L]] | +0.51 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[SPSB1]] | +0.51 | +0.49 / +0.40 | both halves | 4e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ABHD5]] | +0.51 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[WDR47]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SLC9A1]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SDCBP]] | +0.50 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FAM53C]] | +0.50 | +0.60 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF7]] | -0.50 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[HMGXB3]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SETD1A]] | -0.46 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[HNRNPF]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SUGP2]] | -0.45 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[SYMPK]] | -0.45 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[TOMM40]] | -0.45 | -0.41 / -0.49 | both halves | 4e-05 | pathway: Protein localization |
| [[RBM15]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[TRMT61B]] | -0.44 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[PFAS]] | -0.42 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[DDX19A]] | -0.42 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[OPA3]] | -0.42 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSL]] | B | CTSL activity raises UBE2D1's level | lines that do not express CTSL (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without CTSL | 0.017 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, -32.8); signed map (5.6, 20.0). **Vector** length 109, 31.6% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +6.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +1.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:58,334,979-58,370,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH5A, UBCH5, UBC4/5, E2(17)KB1; previously SFT |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 85 pathways, smallest: TICAM1, RIP1-mediated IKK complex recruitment; Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [P51668](https://www.uniprot.org/uniprotkb/P51668) (Ubiquitin-conjugating enzyme E2 D1):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-48'-linked polyubiquitination. Mediates the selective degradation of short-lived and abnormal proteins. Functions in the E6/E6-AP-induced ubiquitination of p53/TP53. Mediates ubiquitination of PEX5 and auto-ubiquitination of STUB1, TRAF6 and TRIM63/MURF1. Ubiquitinates STUB1-associated HSP90AB1 in vitro. Lacks inherent specificity for any particular lysine residue of ubiquitin. …

**Summary**, from NCBI Gene [7321](https://www.ncbi.nlm.nih.gov/gene/7321):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is closely related to a stimulator of iron transport (SFT), and is up-regulated in hereditary …

**Accessions** — [HGNC:12474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12474) · Entrez [7321](https://www.ncbi.nlm.nih.gov/gene/7321) · UniProt [P51668](https://www.uniprot.org/uniprotkb/P51668) · Ensembl [ENSG00000072401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072401)

## Data

Gene col 1017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1017); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1017]; `tensor/DDL_lfc|DDL_z.npy` [1017]; `embed/gene_vectors.npy` [1017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1017 or target_col == 1017). Every well: [[UBE2D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
