---
symbol: "BTG2"
type: "gene"
col: 8251
ensembl_id: "ENSG00000159388"
name: "BTG anti-proliferation factor 2"
location: "1q32.1"
module: 62
arm: "+"
pooled_cpm: 10.56
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# BTG2

*BTG anti-proliferation factor 2* — 1q32.1

> [!summary] In one line
> BTG2 is an antiproliferative immediate-early gene and direct p53 target that works by accelerating mRNA deadenylation rather than by inhibiting a kinase.

## What it is

BTG2 (also PC3, TIS21) belongs to the BTG/Tob antiproliferative family. It has no enzymatic activity of its own; it is an adapter built around the conserved BTG domain (boxes A and B). Its best-established molecular function is bridging the poly(A)-binding protein PABPC1 to CNOT7/CNOT8 (Caf1a/Caf1b), the catalytic deadenylase subunits of the CCR4–NOT complex. Through that bridge BTG2 acts as a general activator of mRNA deadenylation, and the PABPC1 interaction is required for its antiproliferative effect — so BTG2 restrains proliferation post-transcriptionally, which makes it mechanistically unlike the CDK-inhibitor arm of the p53 response.

Its transcriptional behaviour is the other half of the story. BTG2 was first catalogued as an immediate-early gene (TIS21 for TPA-inducible sequence 21) induced by growth factors, serum and phorbol esters, and separately as a p53-dependent DNA-damage-response gene with a p53 response element in its promoter. Functionally, the clearest downstream account is that BTG2 limits cyclin D1 expression and so holds RB hypophosphorylated, enforcing G1 arrest. A systematic screen for the effectors that actually carry p53's antiproliferative output identified BTG2 as a major one in Ras-transduced mouse and human fibroblasts: knocking it down cooperated with oncogenic Ras to transform cells that still had transcriptionally active p53. Later work reported that BTG2 binds H-Ras and lowers its GTP loading, giving a second, more direct route to the same effect. BTG2 expression is reported reduced in a sizeable fraction of kidney and breast carcinomas, and the gene also has roles in neurogenesis and in maintaining quiescence.

## What is uncertain

The p53-dependence of BTG2 induction is solid for DNA damage in specific systems, but the gene's immediate-early character means an induction at 24 h cannot be attributed to p53 from the induction alone. The deadenylation mechanism is well supported biochemically; which mRNAs it actually controls in a cell is largely unmapped, and cyclin D1 repression — the usual stated link to arrest — rests heavily on overexpression experiments. BTG2's standing as a tumour suppressor comes from expression-loss correlations and mouse fibroblast genetics rather than recurrent somatic mutation; the gene is rarely mutated in human tumours. The Ras-GTP-loading claim has been reported in a small number of systems and should be treated as provisional.

## References

- Rouault et al., 1996, Nature Genetics — cloned human BTG2 and showed its expression is p53-dependent in the DNA-damage response.
- Boiko et al., 2006, Genes & Development — identified BTG2 as a major downstream effector of p53-dependent arrest of Ras-transformed fibroblasts, acting via cyclin D1/E1 and RB.
- Mauxion, Faux & Séraphin, 2008, The EMBO Journal — showed BTG2 is a general activator of mRNA deadenylation.
- Winkler, 2010, Journal of Cellular Physiology — review of the BTG/Tob antiproliferative protein family and its CCR4–NOT link.
- Fischer, 2017, Oncogene — census of p53 target genes, placing BTG2 among the well-supported direct targets.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.95× (z +24.5, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.555× (z -6.4, q 8e-08, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRM2B]] (+0.68, fdr 7e-06), [[SPATA18]] (+0.66, fdr 1e-05), [[PINCR]] (+0.65, fdr 1e-05); moves opposite to [[DROSHA]] (-0.50, fdr 3e-05), [[INVS]] (-0.50, fdr 4e-05), [[HERC2P3]] (-0.49, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[DRAM1]] → it (grade B ⚠); 3 go from it, the strongest it → [[BBC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.95×** | +24.5 | 0e+00 | 32/35 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.35×** | +12.6 | 7e-34 | 34/39 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.07×** | +12.1 | 1e-31 | 23/35 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +10.1 | 8e-22 | 25/36 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.2 | 3e-14 | 22/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.3 | 2e-11 | 15/29 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +7.1 | 1e-10 | 23/41 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.2 | 1e-05 | 18/40 (A498, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-05 | 18/40 (Hs 766T, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 8e-05 | 19/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 9e-05 | 19/40 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.4 | 4e-04 | 19/39 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.1 | 0.001 | 13/38 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Cytarabine (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.001 | 14/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.0 | 0.003 | 6/19 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 9/39 (SW480, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.006 | 10/39 (NCI-H460, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.008 | 12/40 (NCI-H460, A498, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.555×** | -6.4 | 8e-08 | 20/38 (HT-29, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -5.5 | 1e-05 | 20/40 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.627×** | -4.8 | 3e-04 | 20/37 (SW48, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.748× | -3.2 | 0.20 | 16/39 (LoVo, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.3 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +16.6) | — |
| [[A498 (line)]] | wt | 13.0 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -11.5) |
| [[A549 (line)]] | wt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +12.9) | [[Sunitinib (drug)]] 5 µM 0.0573× (z -9.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 21.1 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.0264× (z -13.2) |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.154× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 3.22 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +12.6) | [[Omeprazole (drug)]] 0.5 µM 0.0792× (z -9.5) |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.182× (z -8.8) |
| [[LoVo (line)]] | wt | 29.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -9.9) |
| [[LS 180 (line)]] | wt | 21.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.54× (z +8.8) ⚠ toxic | [[Bortezomib (drug)]] 5 µM 0.0444× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 5.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +14.8) | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +11.1) | — |
| [[C32 (line)]] | wt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 6.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +21.2) | — |
| [[Hs 766T (line)]] | wt | 7.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 5.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 3.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 5.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 8.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +8.6) | — |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRM2B]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[PINCR]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ABCA12]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LRATD1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CDIP1]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PTCHD4]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[XPC]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PLXNB2]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PHLDA3]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 407 |
| [[GRIN2C]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[FDXR]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DROSHA]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[INVS]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HERC2P3]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RNF216]] | -0.48 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CACYBP]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HACD3]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[EEF1E1]] | -0.48 | -0.51 / -0.35 | both halves | 1e-04 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[NTAQ1]] | -0.48 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[DCUN1D5]] | -0.47 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[IQCB1]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[LRRC20]] | -0.47 | -0.48 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DRAM1]] | B | DRAM1 activity lowers BTG2's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.27× higher at baseline in the lines without DRAM1 | 0.008 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[ACTA2]] | B | ACTA2 activity strengthens BTG2's drug response | lines that do not express ACTA2 (10) vs lines expressing it (31) | the lines without ACTA2 respond 0.32× as strongly (z diff +2.06); strongest at Topotecan (hydrochloride) 5 µM: 0.53x vs 2.08x (z diff +6.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[PINCR]] | B | PINCR activity raises BTG2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.96× lower at baseline in the lines without PINCR | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PSMB5]] | B | PSMB5 activity raises BTG2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers BTG2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAS]] | B | FAS activity strengthens BTG2's drug response | lines that do not express FAS (7) vs lines expressing it (34) | the lines without FAS respond 0.07× as strongly (z diff +2.51); strongest at Topotecan (hydrochloride) 5 µM: 0.30x vs 1.93x (z diff +7.8) | 0.028 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DRAM1]] | B | DRAM1 activity strengthens BTG2's drug response | lines that do not express DRAM1 (6) vs lines expressing it (35) | the lines without DRAM1 respond 0.00× as strongly (z diff +3.10); strongest at Topotecan (hydrochloride) 5 µM: 0.32x vs 2.06x (z diff +8.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NTN1]] | B | NTN1 activity strengthens BTG2's drug response | lines that do not express NTN1 (14) vs lines expressing it (27) | the lines without NTN1 respond 0.54× as strongly (z diff +1.51); strongest at Idarubicin (hydrochloride) 5 µM: 1.07x vs 2.21x (z diff +4.3) | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises BTG2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without PTCHD4 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[TP53]] | C | TP53 activity strengthens BTG2's drug response | recorded loss-of-function mutation of TP53 in 24 lines vs 17 not recorded | the TP53-altered lines respond 0.46× as strongly (z diff +2.10); strongest at Topotecan (hydrochloride) 5 µM: 0.92x vs 2.98x (z diff +5.6) | 0.589 over the table, 0.031 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BBC3]] | B | BTG2 activity raises BBC3's level | lines that do not express BTG2 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without BTG2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CYFIP2, SLC37A1; maybe low, not absent |
| [[PPM1D]] | B | BTG2 activity raises PPM1D's level | lines that do not express BTG2 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without BTG2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CYFIP2, SLC37A1; maybe low, not absent |
| [[CYFIP2]] | C | BTG2 activity raises CYFIP2's level | lines that do not express BTG2 (6) vs lines expressing it (44) | 4.51× lower at baseline in the lines without BTG2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CYFIP2, SLC37A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, 37.6); signed map (43.2, -22.2). **Vector** length 114, 29.8% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +24.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.1 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BTG anti-proliferation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,305,491-203,309,602 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC3, TIS21, MGC126063, MGC126064, APRO1 |
| Gene groups (HGNC) | BTG/Tob family |
| Hallmark sets | KRAS_SIGNALING_DN, INFLAMMATORY_RESPONSE, APOPTOSIS, UV_RESPONSE_UP, HEME_METABOLISM, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; TP53 Regulates Transcription of Cell Cycle Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [P78543](https://www.uniprot.org/uniprotkb/P78543) (Protein BTG2):

> Anti-proliferative protein; the function is mediated by association with deadenylase subunits of the CCR4-NOT complex. Activates mRNA deadenylation in a CNOT6 and CNOT7-dependent manner. In vitro can inhibit deadenylase activity of CNOT7 and CNOT8. Involved in cell cycle regulation. Could be involved in the growth arrest and differentiation of the neuronal precursors (By similarity). Modulates transcription regulation mediated by ESR1. Involved in mitochondrial depolarization and neurite …

**Summary**, from NCBI Gene [7832](https://www.ncbi.nlm.nih.gov/gene/7832):

> The protein encoded by this gene is a member of the BTG/Tob family. This family has structurally related proteins that appear to have antiproliferative properties. This encoded protein is involved in the regulation of the G1/S transition of the cell cycle. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1131) · Entrez [7832](https://www.ncbi.nlm.nih.gov/gene/7832) · UniProt [P78543](https://www.uniprot.org/uniprotkb/P78543) · Ensembl [ENSG00000159388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159388)

## Data

Gene col 8251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8251); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8251]; `tensor/DDL_lfc|DDL_z.npy` [8251]; `embed/gene_vectors.npy` [8251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8251 or target_col == 8251). Every well: [[BTG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/BTG2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
