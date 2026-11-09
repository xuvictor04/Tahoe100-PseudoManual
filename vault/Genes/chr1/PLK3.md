---
symbol: "PLK3"
type: "gene"
col: 10432
ensembl_id: "ENSG00000173846"
name: "polo like kinase 3"
location: "1p34.1"
module: 141
arm: "+"
pooled_cpm: 20.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/141", "written"]
generated_by: "tahoemap"
---

# PLK3

*polo like kinase 3* — 1p34.1

> [!summary] In one line
> PLK3 encodes a stress-activated polo-like kinase, switched on by DNA damage and oxidative stress, that has been implicated in phosphorylating p53 at serine 20.

## What it is

PLK3 (also PRK, FNK, CNK) belongs to the polo-like kinase family — an N-terminal kinase domain plus a C-terminal polo-box domain for substrate docking and localisation. Family membership is misleading if read as family resemblance. PLK1 is a mitotic kinase, overexpressed in tumours and a drug target; PLK3 behaves instead as a stress-response kinase whose transcript is an immediate-early gene and whose activity is induced rather than cell-cycle-scheduled.

The best-developed part of its biology is the damage response. PLK3 activity rises rapidly after DNA damage in an ATM-dependent manner, and PLK3 phosphorylates p53 on serine 20 in vitro — the site whose modification interferes with [[MDM2]] binding and so stabilises the protein. Hydrogen peroxide produces a comparable activation, and in cells a kinase-dead PLK3 reduces serine 20 phosphorylation after either insult, though the published effect is partial in both cases. PLK3 has also been reported to phosphorylate CHK2 ([[CHEK2]]) and CDC25C and to act on HIF-1α under hypoxia, but no single function has been pinned down as its principal one.

PLK3 is usually labelled a tumour suppressor. The basis is expression rather than mutation — the transcript is reported down-regulated in several carcinomas, lung and head and neck among them. The mouse genetics are split rather than merely weak: one study reports tumours in various organs in aged Plk3-null animals, tied to deregulated HIF-1α, while another finds no significant increase in spontaneous tumour incidence across genotypes.

## What is uncertain

The serine 20 claim deserves its hedges. It rests on in vitro kinase work plus dominant-negative and knockdown experiments; CHK2 is the better-established serine 20 kinase, and how much PLK3 contributes in any particular cell type is unresolved; the two are not mutually exclusive. Whether PLK3 is a *direct* p53 target is a separate, weaker question: it is damage-inducible, but a validated p53 response element is not part of the standard account, so membership in a p53-associated induction arm may reflect a general stress induction running parallel to p53 rather than through it. The tumour-suppressor designation rests largely on reduced expression in tumour series, and the mouse data do not settle it either way. Most pointedly here, a report has PLK3 phosphorylating serine 20 of gain-of-function mutant p53 and supporting its transactivation — if that holds, PLK3's effect is conditional on p53 genotype, and this panel contains both wild-type and altered lines (see [[p53 nullification in cancer cell lines]]).

## References

- Xie et al., 2001, Journal of Biological Chemistry — Plk3 links DNA damage to arrest and apoptosis partly via p53, with ATM-dependent activation and serine 20 as a target site.
- Xie et al., 2001, Journal of Biological Chemistry — reactive-oxygen-species-induced phosphorylation of p53 on serine 20 is mediated in part by Plk3.
- Bahassi El et al., 2002, Oncogene — Plk3 as a multifunctional kinase in stress-response pathways, interacting with the damage checkpoint machinery.
- Myer et al., 2011, Mutation Research — Plk3-null mice stabilise Cdc25A after DNA damage, but show no significant increase in tumour incidence between genotypes.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.03× (z +15.6, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.439× (z -7.8, q 3e-12, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTBD19]] (+0.78, fdr 7e-06, ⚠ same locus), [[DUSP5]] (+0.68, fdr 7e-06), [[EGR2]] (+0.66, fdr 7e-06), [[GALE]] (+0.65, fdr 7e-06); moves opposite to [[PAIP1]] (-0.51, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.03×** | +15.6 | 0e+00 | 36/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.63×** | +9.2 | 6e-18 | 32/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +7.9 | 4e-13 | 27/46 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.76×** | +5.6 | 2e-06 | 30/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +5.0 | 7e-05 | 25/48 (A-172, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.1 | 0.004 | 18/44 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.49×** | +4.0 | 0.005 | 23/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +3.9 | 0.007 | 20/45 (A-172, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.47×** | +3.8 | 0.007 | 23/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.007 | 21/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.45×** | +3.7 | 0.010 | 19/46 (NCI-H2347, NCI-H460, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.014 | 19/44 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.27×** | +3.3 | 0.037 | 20/46 (NCI-H460, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.439×** | -7.8 | 3e-12 | 37/45 (SW480, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.465×** | -7.5 | 2e-11 | 35/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.483×** | -7.2 | 1e-10 | 34/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.477×** | -7.0 | 3e-10 | 36/47 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.505×** | -6.8 | 1e-09 | 27/47 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.627×** | -6.4 | 1e-08 | 39/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.588×** | -6.4 | 2e-08 | 34/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.548×** | -6.0 | 2e-07 | 33/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.562×** | -5.3 | 8e-06 | 30/47 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.339×** | -5.0 | 3e-05 | 30/44 (HT-29, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.593×** | -4.9 | 5e-05 | 26/47 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.686×** | -3.9 | 0.005 | 26/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.741×** | -3.8 | 0.007 | 20/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.450×** | -3.7 | 0.008 | 20/47 (HOP62, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.700×** | -3.5 | 0.016 | 21/37 (NCI-H2347, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.486×** | -3.4 | 0.027 | 13/47 (NCI-H2347, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.3 | 0 | 6 | — | [[Cobimetinib (drug)]] 5 µM 0.127× (z -11.4) |
| [[HT-29 (line)]] | alt | 54.5 | 0 | 4 (3 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.177× (z -9.9) |
| [[A-172 (line)]] | wt | 18.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 28.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -10.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.43 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 7.07× (z +11.5) | — |
| [[A498 (line)]] | wt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +14.7) | — |
| [[A549 (line)]] | wt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 41.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0697× (z -17.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 25.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.8) | — |
| [[J82 (line)]] | alt | 16.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +16.2) | — |
| [[SNU-423 (line)]] | alt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 8.94 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +9.3) | [[Cobimetinib (drug)]] 0.5 µM 0.112× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +17.3) | — |
| [[HEC-1-A (line)]] | alt | 8.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +10.7) | — |
| [[KATO III (line)]] | alt | 19.5 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.131× (z -10.9) |
| [[LS 180 (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 9.63 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.3) | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0432× (z -10.6) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD19]] | +0.78 | +0.82 / +0.80 | both halves | 7e-06 | ⚠ same locus (2.5 kb, same strand: neighbours can correlate without regulation) |
| [[DUSP5]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 | STRING 568 |
| [[EGR2]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[GALE]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[EGR3]] | +0.64 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[EHD1]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RIN1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 | STRING 524 |
| [[ITPKC]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[EFNB1]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MAP2K3]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 | STRING 444 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity strengthens PLK3's drug response | lines that do not express TINAGL1 (26) vs lines expressing it (22) | the lines without TINAGL1 respond 0.65× as strongly (z diff +1.08); strongest at Cobimetinib 0.5 µM: 0.66x vs 0.41x (z diff +2.3) | 0.012 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; target measured in part of the lines |
| [[TGFA]] | B | TGFA activity strengthens PLK3's drug response | lines that do not express TGFA (17) vs lines expressing it (31) | the lines without TGFA respond 0.77× as strongly (z diff +0.82); strongest at Trametinib (DMSO_TF solvate) 0.5 µM: 0.67x vs 0.40x (z diff +2.2) | 0.014 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1; target measured in part of the lines |
| [[INPP1]] | B | INPP1 activity raises PLK3's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without INPP1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises PLK3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TINAGL1]] | B | TINAGL1 activity raises PLK3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without TINAGL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[EPHB3]] | B | EPHB3 activity raises PLK3's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.16× lower at baseline in the lines without EPHB3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[PRAG1]] | B | PRAG1 activity strengthens PLK3's drug response | lines that do not express PRAG1 (16) vs lines expressing it (32) | the lines without PRAG1 respond 0.66× as strongly (z diff +1.28); strongest at Cobimetinib 5 µM: 0.49x vs 0.38x (z diff +1.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EFNB2]] | B | EFNB2 activity raises PLK3's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without EFNB2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[CD22]] | B | CD22 activity strengthens PLK3's drug response | lines that do not express CD22 (21) vs lines expressing it (27) | the lines without CD22 respond 0.56× as strongly (z diff +1.65); strongest at Trametinib (DMSO_TF solvate) 5 µM: 0.59x vs 0.37x (z diff +2.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, -1.0); signed map (6.2, 32.4). **Vector** length 125, 36.7% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +15.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.1 | +5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.3 | +1.1 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -6.8 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.6 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.2 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.0 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.8 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.6 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | polo like kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,800,377-44,805,990 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FNK, PRK; previously CNK |
| Gene groups (HGNC) | Polo like kinase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 10 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; TP53 Regulates Transcription of Cell Cycle Genes; Ubiquitin-Mediated Degradation of Phosphorylated Cdc25A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4B4](https://www.uniprot.org/uniprotkb/Q9H4B4) (Serine/threonine-protein kinase PLK3):

> Serine/threonine-protein kinase involved in cell cycle regulation, response to stress and Golgi disassembly. Polo-like kinases act by binding and phosphorylating proteins that are already phosphorylated on a specific motif recognized by the POLO box domains. Phosphorylates ATF2, BCL2L1, CDC25A, CDC25C, CHEK2, HIF1A, JUN, p53/TP53, p73/TP73, PTEN, TOP2A and VRK1. Involved in cell cycle regulation: required for entry into S phase and cytokinesis. Phosphorylates BCL2L1, leading to regulate the G2 …

**Summary**, from NCBI Gene [1263](https://www.ncbi.nlm.nih.gov/gene/1263):

> The protein encoded by this gene is a member of the highly conserved polo-like kinase family of serine/threonine kinases. Members of this family are characterized by an amino-terminal kinase domain and a carboxy-terminal bipartite polo box domain that functions as a substrate-binding motif and a cellular localization signal. Polo-like kinases are important regulators of cell cycle progression. This gene has also been implicated in stress responses and double-strand break repair. In human cell …

**Accessions** — [HGNC:2154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2154) · Entrez [1263](https://www.ncbi.nlm.nih.gov/gene/1263) · UniProt [Q9H4B4](https://www.uniprot.org/uniprotkb/Q9H4B4) · Ensembl [ENSG00000173846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173846)

## Data

Gene col 10432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10432); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10432]; `tensor/DDL_lfc|DDL_z.npy` [10432]; `embed/gene_vectors.npy` [10432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10432 or target_col == 10432). Every well: [[PLK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PLK3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
