---
symbol: "PDCD6IP-DT"
type: "gene"
col: 15691
ensembl_id: "ENSG00000271643"
name: "PDCD6IP divergent transcript"
location: "3p22.3"
module: 35
arm: "+"
pooled_cpm: 8.51
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PDCD6IP-DT

*PDCD6IP divergent transcript* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.75× (z +6.7, q 9e-09, up in 24 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.326× (z -13.5, q 1e-38, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM217]] (+0.74, fdr 7e-06), [[LINC00571]] (+0.65, fdr 1e-05), [[ATXN1L]] (+0.65, fdr 3e-05); moves opposite to [[CHEK2]] (-0.64, fdr 1e-05), [[ATG4C]] (-0.57, fdr 3e-05), [[SPATA6]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GATA2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +6.7 | 9e-09 | 24/44 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.0 | 6e-07 | 19/41 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +5.4 | 1e-05 | 22/46 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.2 | 3e-05 | 11/25 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.007 | 7/46 (KATO III, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.008 | 13/44 (LS 180, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.5 | 0.039 | 10/33 (KATO III, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.4 | 0.045 | 6/18 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.057 | 5/46 (LS 180, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.059 | 7/47 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.062 | 9/42 (SW 900, C-33 A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.31×** | +3.1 | 0.093 | 12/42 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.326×** | -13.5 | 1e-38 | 41/46 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.383×** | -11.5 | 3e-28 | 37/44 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.414×** | -10.6 | 6e-24 | 38/46 (SW480, BT-474, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.522×** | -7.5 | 8e-12 | 24/44 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.536×** | -7.5 | 8e-12 | 28/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.591×** | -6.3 | 2e-08 | 23/40 (SW480, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.615×** | -5.8 | 4e-07 | 20/44 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.710×** | -5.8 | 4e-07 | 22/46 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.623×** | -5.7 | 8e-07 | 22/42 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.653×** | -4.9 | 5e-05 | 21/36 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.673×** | -4.8 | 1e-04 | 20/46 (LoVo, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.020 | 12/41 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.772×** | -3.1 | 0.085 | 8/44 (SW1417, HS-578T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.2 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.146× (z -15.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.207× (z -12.3) |
| [[BT-474 (line)]] | alt | 6.19 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0396× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0729× (z -8.8) |
| [[COLO 205 (line)]] | alt | 7.54 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0617× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0794× (z -8.5) |
| [[KATO III (line)]] | alt | 14.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 9.60 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.1000× (z -11.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -11.2) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.160× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 2.48 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0627× (z -9.3) |
| [[C-33 A (line)]] | alt | 7.21 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0766× (z -8.7) |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0854× (z -8.6) |
| [[HT-29 (line)]] | alt | 8.74 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0541× (z -12.0) |
| [[J82 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0764× (z -12.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 5.42 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0388× (z -11.9) |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -13.1) |
| [[A-427 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM217]] | +0.74 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LINC00571]] | +0.65 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.65 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PBLD]] | +0.64 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | +0.64 | +0.51 / +0.37 | both halves | 8e-05 | same gene group |
| [[SMC5-DT]] | +0.62 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[EIF5]] | +0.62 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[LINC00863]] | +0.61 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[C2orf49-DT]] | +0.61 | +0.42 / +0.41 | both halves | 4e-05 | same gene group |
| [[ACYP2]] | +0.61 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[UBE2D3-AS1]] | +0.60 | +0.39 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHEK2]] | -0.64 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.57 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SPATA6]] | -0.56 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RSAD1]] | -0.56 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[PLEKHH3]] | -0.56 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ORC4]] | -0.55 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[HACE1]] | -0.55 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[IFT172]] | -0.55 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[PAXX]] ⚠ | -0.55 | -0.27 / -0.40 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CEP131]] | -0.54 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[HMGN3]] | -0.54 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[NBPF3]] | -0.54 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[C6orf136]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA2-AS1]] | B | GATA2-AS1 activity lowers PDCD6IP-DT's level | lines that do not express GATA2-AS1 (10) vs lines expressing it (40) | 1.36× higher at baseline in the lines without GATA2-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: GATA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.8, 10.9); signed map (22.7, -6.8). **Vector** length 82.9, 15.9% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.7 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.3 | -10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -13.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | PDCD6IP divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p22.3 — chr3:33,793,644-33,798,539 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-10C24.1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55244) · Entrez [105377023](https://www.ncbi.nlm.nih.gov/gene/105377023) · Ensembl [ENSG00000271643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271643)

## Data

Gene col 15691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15691); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15691]; `tensor/DDL_lfc|DDL_z.npy` [15691]; `embed/gene_vectors.npy` [15691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15691 or target_col == 15691). Every well: [[PDCD6IP-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD6IP-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
