---
symbol: "NT5DC2"
type: "gene"
col: 9621
ensembl_id: "ENSG00000168268"
name: "5'-nucleotidase domain containing 2"
location: "3p21.1"
module: 42
arm: "+"
pooled_cpm: 7.24
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# NT5DC2

*5'-nucleotidase domain containing 2* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.63× (z +18.1, q 0e+00, up in 27 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.74× (z +6.5, q 1e-08, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.489× (z -12.0, q 4e-30, down in 33 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOGS]] (+0.64, fdr 7e-06), [[CHPF2]] (+0.63, fdr 7e-06), [[RER1]] (+0.62, fdr 1e-05); moves opposite to [[H3-3B]] (-0.53, fdr 1e-05), [[CEBPD]] (-0.53, fdr 2e-05), [[RBM43]] (-0.52, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[P3H4]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.63×** | +18.1 | 0e+00 | 27/29 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +16.6 | 0e+00 | 15/15 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +11.8 | 1e-29 | 18/21 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +6.5 | 1e-08 | 25/44 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.6 | 3e-06 | 16/31 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +5.5 | 3e-06 | 17/34 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[OTS514 (drug)]] 5 µM |  | **2.05×** | +4.4 | 0.001 | 10/33 (NCI-H1792, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.40×** | +3.9 | 0.006 | 9/44 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.006 | 6/41 (HOP62, LOX-IMVI, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.007 | 8/43 (KATO III, Panc 03.27, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.024 | 10/42 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.035 | 5/41 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.3 | 0.043 | 3/17 (HOP62, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.066 | 4/41 (A-172, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.096 | 5/43 (SK-MEL-2, C32, …) | two highest doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.489×** | -12.0 | 4e-30 | 33/41 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -7.5 | 1e-11 | 22/40 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.560×** | -6.6 | 8e-09 | 23/42 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.704×** | -4.2 | 0.004 | 17/44 (C-33 A, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.738×** | -3.6 | 0.035 | 8/46 (LS 180, C32, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.578×** | -3.3 | 0.077 | 6/44 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.086 | 11/44 (SNU-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.52 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.4) |
| [[HOP62 (line)]] | alt | 17.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0546× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 11.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.6) |
| [[HS-578T (line)]] | alt | 11.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 8.51 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.84× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.2) |
| [[A-172 (line)]] | wt | 6.34 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0960× (z -9.2) |
| [[BT-474 (line)]] | alt | 3.77 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0419× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -8.8) |
| [[KATO III (line)]] | alt | 9.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 7.29 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.122× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 6.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 9.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.33× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 3.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.4) |
| [[SHP-77 (line)]] | alt | 7.36 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0790× (z -9.4) |
| [[SW 900 (line)]] | alt | 5.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -9.1) |
| [[SW48 (line)]] | wt | 13.2 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0547× (z -8.9) |
| [[A498 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOGS]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CHPF2]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RER1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SMPD4]] | +0.60 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[DDB1]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[B4GALT2]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[AKT1]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PPP4C]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TMEM248]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SURF4]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[AMPD2]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[GNAS-AS1]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CEBPD]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RBM43]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[STX17]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SP100]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NMI]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PSMB8]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[SCAF11]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[DDX60]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PPCS]] | -0.47 | -0.45 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H4]] | C | P3H4 activity raises NT5DC2's level | lines that do not express P3H4 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without P3H4 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, TMCC2, E2F7; maybe low, not absent |
| [[P3H1]] | C | P3H1 activity raises NT5DC2's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without P3H1 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.6, -28.1); signed map (-51.0, 2.6). **Vector** length 59.3, 9.04% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +11.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,524,385-52,535,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12442 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H857](https://www.uniprot.org/uniprotkb/Q9H857) (5'-nucleotidase domain-containing protein 2):

> Promotes dephosphorylation of tyrosine 3-monooxygenase TH which decreases TH catalytic activity and leads to reduced synthesis of catecholamines including dopamine, noradrenaline and adrenaline. The exact mechanism of activity is unknown but may act as a phosphatase or promote the activity of phosphatases or may inhibit phosphorylation by acting as a barrier to interfere with protein kinase access.

**Summary**, from NCBI Gene [64943](https://www.ncbi.nlm.nih.gov/gene/64943):

> Predicted to enable 5'-nucleotidase activity. Predicted to be involved in negative regulation of dopamine biosynthetic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25717) · Entrez [64943](https://www.ncbi.nlm.nih.gov/gene/64943) · UniProt [Q9H857](https://www.uniprot.org/uniprotkb/Q9H857) · Ensembl [ENSG00000168268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168268)

## Data

Gene col 9621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9621); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9621]; `tensor/DDL_lfc|DDL_z.npy` [9621]; `embed/gene_vectors.npy` [9621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9621 or target_col == 9621). Every well: [[NT5DC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5DC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
