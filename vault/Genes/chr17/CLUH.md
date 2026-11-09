---
symbol: "CLUH"
type: "gene"
col: 5307
ensembl_id: "ENSG00000132361"
name: "CLUH binding protein of NUMT mRNA"
location: "17p13.3"
module: 1
arm: "+"
pooled_cpm: 22.96
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CLUH

*CLUH binding protein of NUMT mRNA* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.42× (z +12.6, q 2e-33, up in 28 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.89× (z +9.4, q 9e-19, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.770× (z -3.9, q 0.053, down in 12 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.318×, RKO 0.426×; ⚠ cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (C-33 A 0.140×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.211×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBBP1A]] (+0.76, fdr 7e-06), [[TRMT61A]] (+0.74, fdr 7e-06), [[PUS1]] (+0.73, fdr 7e-06); moves opposite to [[GNAS]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.42×** | +12.6 | 2e-33 | 28/34 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.24×** | +11.9 | 4e-30 | 40/42 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.98×** | +10.1 | 9e-22 | 42/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +9.7 | 6e-20 | 34/47 (AsPC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.4 | 9e-19 | 36/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.93×** | +8.9 | 4e-17 | 28/39 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.70×** | +7.8 | 4e-13 | 33/48 (C32, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +7.7 | 9e-13 | 34/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.64×** | +7.0 | 2e-10 | 28/45 (LoVo, NCI-H460, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.45×** | +6.7 | 9e-10 | 36/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.7 | 9e-10 | 31/47 (NCI-H1792, SW480, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +5.9 | 1e-07 | 26/46 (NCI-H1792, NCI-H460, …) | two highest doses | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.9 | 2e-07 | 27/44 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.8 | 2e-07 | 29/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.47×** | +5.7 | 5e-07 | 24/47 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.66×** | +5.3 | 3e-06 | 23/47 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.03×** | +5.3 | 3e-06 | 27/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.99×** | +5.2 | 6e-06 | 27/46 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.2 | 6e-06 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 2e-05 | 26/47 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.93×** | +4.9 | 2e-05 | 22/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 1e-04 | 21/45 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 2e-04 | 20/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.79×** | +4.4 | 3e-04 | 21/46 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.002 | 18/47 (NCI-H1792, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.318×, RKO 0.426×; ⚠ cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (C-33 A 0.140×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.211×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.770×** | -3.9 | 0.053 | 12/48 (NCI-H460, HT-29, …) | two highest doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.792× | -3.4 | 0.22 | 13/46 (C-33 A, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 27.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.58× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.67× (z +9.8) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 34.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.140× (z -11.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBBP1A]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 | STRING 518 |
| [[TRMT61A]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[PUS1]] | +0.73 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[RRP1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SNHG17]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[IMP4]] | +0.72 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[BOP1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | same gene group |
| [[PFAS]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RBM28]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PUM3]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[NLE1]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[WDR4]] | +0.68 | +0.69 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.1, -39.1); signed map (-2.9, -45.0). **Vector** length 92.5, 22.2% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 23); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.53 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +10.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.7 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.5 | +12.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.5 | +5.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CLUH binding protein of NUMT mRNA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,689,386-2,712,663 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLU1; previously KIAA0664 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75153](https://www.uniprot.org/uniprotkb/O75153) (Clustered mitochondria protein homolog):

> mRNA-binding protein involved in proper cytoplasmic distribution of mitochondria. Specifically binds mRNAs of nuclear-encoded mitochondrial proteins in the cytoplasm and regulates transport or translation of these transcripts close to mitochondria, playing a role in mitochondrial biogenesis.

**Summary**, from NCBI Gene [23277](https://www.ncbi.nlm.nih.gov/gene/23277):

> Enables mRNA binding activity. Involved in intracellular distribution of mitochondria and mitochondrion organization. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29094) · Entrez [23277](https://www.ncbi.nlm.nih.gov/gene/23277) · UniProt [O75153](https://www.uniprot.org/uniprotkb/O75153) · Ensembl [ENSG00000132361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132361)

## Data

Gene col 5307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5307); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5307]; `tensor/DDL_lfc|DDL_z.npy` [5307]; `embed/gene_vectors.npy` [5307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5307 or target_col == 5307). Every well: [[CLUH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLUH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
