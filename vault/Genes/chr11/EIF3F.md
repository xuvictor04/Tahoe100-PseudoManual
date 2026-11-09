---
symbol: "EIF3F"
type: "gene"
col: 10605
ensembl_id: "ENSG00000175390"
name: "eukaryotic translation initiation factor 3 subunit F"
location: "11p15.4"
module: 20
arm: "+"
pooled_cpm: 27.4
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF3F

*eukaryotic translation initiation factor 3 subunit F* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.63× (z +16.3, q 0e+00, up in 37 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.83× (z +15.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.799× (z -5.9, q 3e-06, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.145×, Panc 03.27 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Bimatoprost (drug)]] 0.05 µM in 1 line (NCI-H661 0.0547×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.213×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIDO1]] (+0.70, fdr 2e-05), [[TSN]] (+0.68, fdr 7e-06), [[C1D]] (+0.66, fdr 1e-05); moves opposite to [[METTL23]] (-0.67, fdr 2e-04), [[SLC25A4]] (-0.65, fdr 4e-05), [[BTG1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +16.3 | 0e+00 | 37/41 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.83×** | +15.0 | 0e+00 | 45/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +14.1 | 9e-43 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +12.1 | 1e-31 | 35/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.5 | 1e-28 | 38/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.9 | 9e-26 | 34/44 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +10.5 | 7e-24 | 38/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +10.4 | 2e-23 | 39/47 (SW480, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.8 | 9e-21 | 30/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +9.0 | 2e-17 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.5 | 7e-16 | 29/47 (SNU-423, BT-474, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +8.3 | 5e-15 | 37/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.7 | 5e-13 | 34/45 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.1 | 5e-11 | 30/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.9 | 2e-10 | 31/47 (LoVo, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.7 | 6e-10 | 35/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.1 | 3e-08 | 27/48 (PANC-1, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 6e-06 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.3 | 5e-04 | 14/48 (HOP62, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.004 | 11/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.145×, Panc 03.27 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Bimatoprost (drug)]] 0.05 µM in 1 line (NCI-H661 0.0547×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.213×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -5.9 | 3e-06 | 25/48 (SW1417, NCI-H661, …) | rises with dose |  |
| [[Adenosine (drug)]] 5 µM |  | 0.868× | -3.7 | 0.045 | 12/48 (HS-578T, C-33 A, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.820×** | -3.7 | 0.045 | 18/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM |  | **0.824×** | -3.6 | 0.051 | 13/48 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.21 | 7/48 (A-172, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +16.3) | — |
| [[SW480 (line)]] | alt | 41.0 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.23× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +9.7) | — |
| [[KATO III (line)]] | alt | 13.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 25.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.12× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +8.7) | — |
| [[LoVo (line)]] | wt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +11.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 24.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 20.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.08× (z +8.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.80× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.05 µM 0.0547× (z -8.8) |
| [[RKO (line)]] | wt | 39.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.16× (z +9.3) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.213× (z -8.6) |
| [[A-427 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIDO1]] | +0.70 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[TSN]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[C1D]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.66 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[LY6G5B]] | +0.66 | +0.36 / +0.71 | both halves | 9e-05 |  |
| [[LAMTOR5-AS1]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[SDHD]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NAXD]] | +0.64 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[MED28]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[EEF1A1]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 | STRING 725 |
| [[RPSA]] | +0.63 | +0.48 / +0.71 | both halves | 2e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 980 |
| [[NDUFA10]] | +0.63 | +0.46 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL23]] | -0.67 | -0.31 / -0.78 | both halves | 2e-04 |  |
| [[SLC25A4]] | -0.65 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[BTG1]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[POLD4]] | -0.61 | -0.29 / -0.65 | both halves | 2e-04 |  |
| [[FOXA2]] | -0.60 | -0.29 / -0.72 | both halves | 3e-04 |  |
| [[POLR2H]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.58 | -0.29 / -0.71 | both halves | 2e-04 |  |
| [[TNFRSF1B]] | -0.58 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PLIN3]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[OCEL1]] | -0.57 | -0.22 / -0.59 | both halves | 6e-04 |  |
| [[C19orf81]] | -0.57 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[ORAI1]] | -0.57 | -0.32 / -0.63 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.4, -15.8); signed map (-18.6, -31.1). **Vector** length 77.2, 16.1% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 10); *Peptide chain elongation* (reactome, mean cos +0.51 to 9); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +10.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +15.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | -0.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.6 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:7,970,251-8,001,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-epsilon, eIF3-p47; previously EIF3S5 |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family; Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00303](https://www.uniprot.org/uniprotkb/O00303) (Eukaryotic translation initiation factor 3 subunit F):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [8665](https://www.ncbi.nlm.nih.gov/gene/8665):

> Enables identical protein binding activity and metal-dependent deubiquitinase activity. Contributes to translation initiation factor activity. Involved in IRES-dependent viral translational initiation and translational initiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. Implicated in autosomal recessive intellectual developmental disorder 67. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3275) · Entrez [8665](https://www.ncbi.nlm.nih.gov/gene/8665) · UniProt [O00303](https://www.uniprot.org/uniprotkb/O00303) · Ensembl [ENSG00000175390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175390)

## Data

Gene col 10605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10605); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10605]; `tensor/DDL_lfc|DDL_z.npy` [10605]; `embed/gene_vectors.npy` [10605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10605 or target_col == 10605). Every well: [[EIF3F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
