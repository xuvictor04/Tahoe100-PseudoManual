---
symbol: "USP1"
type: "gene"
col: 8541
ensembl_id: "ENSG00000162607"
name: "ubiquitin specific peptidase 1"
location: "1p31.3"
module: 91
arm: "+"
pooled_cpm: 86.96
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/091", "written"]
generated_by: "tahoemap"
---

# USP1

*ubiquitin specific peptidase 1* — 1p31.3

> [!summary] In one line
> USP1 is a deubiquitinase that, with its cofactor UAF1, strips monoubiquitin from FANCD2/FANCI and from PCNA, resetting the Fanconi-anaemia and translesion-synthesis arms of DNA damage tolerance.

## What it is

USP1 is a cysteine protease of the USP family, nearly inert until it binds WDR48/UAF1 (see [[WDR48]]). Two substrates define it: monoubiquitinated [[FANCD2]]/FANCI, whose deubiquitination is needed to complete crosslink repair, and monoubiquitinated PCNA, whose deubiquitination ends recruitment of the translesion polymerase eta ([[POLH]]). USP1 is therefore a reset switch, not a repair activator or inhibitor; both excess and absence are deleterious. Its own regulation is largely post-translational: it autocleaves after UV damage, letting PCNA-Ub persist, and APC/C degrades it in G1. Its mRNA peaks in S phase. USP1 inhibitors are in clinical development for BRCA1/2-mutant tumours, where losing its activity is synthetic-lethal.

## What is uncertain

USP1 is almost certainly an indirect p53 target: no validated response element is described at the locus, and its downregulation fits loss of E2F-driven transcription and DREAM-mediated repression downstream of p21. A decrease therefore reports cell-cycle exit at least as much as p53 itself, and in a panel where many compounds arrest cells for non-p53 reasons the two are hard to separate. Its activity is also set post-translationally, so the transcript is a weak proxy for how much deubiquitination actually happens.

## References

- Nijman et al., 2005, Molecular Cell — identified USP1 as the deubiquitinase for monoubiquitinated FANCD2.
- Huang et al., 2006, Nature Cell Biology — showed USP1 regulates PCNA monoubiquitination and translesion synthesis, and autocleaves after UV damage.
- Cohn et al., 2007, Molecular Cell — identified UAF1/WDR48 as the cofactor required for USP1 activity.
- Liang et al., 2014, Nature Chemical Biology — ML323, a selective USP1/UAF1 inhibitor, potentiates cisplatin sensitivity.
- Fischer et al., 2016, Nucleic Acids Research — described the p53-p21-DREAM-CDE/CHR route for indirect repression of cell-cycle genes after p53 activation.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +10.5, q 6e-23, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.772× (z -5.9, q 2e-06, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~86% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.780× (z -4.0, q 0.008, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRCA2]] (+0.76, fdr 7e-06), [[RMI1]] (+0.74, fdr 7e-06), [[MASTL]] (+0.73, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +10.5 | 6e-23 | 42/48 (hTERT-HPNE, A549, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.5 | 1e-11 | 39/48 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.52×** | +6.5 | 1e-08 | 39/48 (C32, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.51×** | +6.4 | 2e-08 | 34/47 (C32, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +5.8 | 7e-07 | 29/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.42×** | +5.7 | 1e-06 | 28/49 (RPMI-7951, Panc 03.27, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.5 | 5e-04 | 23/43 (RPMI-7951, SW480, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **1.32×** | +4.5 | 5e-04 | 31/48 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.31×** | +4.2 | 0.002 | 28/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.30×** | +4.1 | 0.002 | 28/50 (SW480, RKO, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 24/48 (SW480, LOX-IMVI, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.29×** | +3.9 | 0.004 | 22/47 (SW480, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.25×** | +3.7 | 0.010 | 24/48 (C32, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.011 | 24/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.17× | +3.6 | 0.012 | 17/48 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.014 | 24/48 (C32, PANC-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.772×** | -5.9 | 2e-06 | 32/48 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.771×** | -4.2 | 0.007 | 29/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.008 | 26/48 (SHP-77, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.780×** | -4.0 | 0.008 | 25/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.719×** | -3.8 | 0.014 | 25/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.055 | 20/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.747×** | -3.4 | 0.055 | 22/48 (Hs 766T, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.674×** | -3.4 | 0.055 | 24/47 (RPMI-7951, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.2 | 0.084 | 19/48 (A498, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.826× | -3.1 | 0.11 | 20/48 (KATO III, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 45.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +15.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.4) | — |
| [[J82 (line)]] | alt | 171 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.25× (z +10.1) | — |
| [[A-172 (line)]] | wt | 93.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.462× (z -10.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A549 (line)]] | wt | 47.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 44.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 65.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.3) | — |
| [[SW480 (line)]] | alt | 99.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.7) | — |
| [[A-427 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.494× (z -10.8) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A498 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.482× (z -12.6) ⚠ cell-cycle shift, explains ~86% of this change |
| [[AsPC-1 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.61× (z +8.8) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[C-33 A (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.345× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 87.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.510× (z -9.6) ⚠ cell-cycle shift, explains ~86% of this change |
| [[HS-578T (line)]] | alt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 76.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 40.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +13.2) | — |
| [[LoVo (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 71.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 68.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.460× (z -9.7) ⚠ cell-cycle shift, explains ~86% of this change |
| [[NCI-H1573 (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 74.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -9.5) |
| [[SNU-423 (line)]] | alt | 56.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRCA2]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 605 |
| [[RMI1]] | +0.74 | +0.66 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MASTL]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ORC6]] | +0.73 | +0.68 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MSH6]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PLK4]] | +0.70 | +0.61 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ESCO2]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[TMPO]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 503 |
| [[NCAPG]] | +0.69 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[LRR1]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.68 | +0.57 / +0.73 | both halves | 1e-05 | STRING 906 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises USP1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without CDC25A | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers USP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises USP1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without E2F8 | 0.086 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-38.9, -47.9); signed map (-42.5, -47.1). **Vector** length 124, 41.1% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.66 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.68 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.68 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.6 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.1 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.7 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -7.8 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.1 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:62,436,297-62,451,804 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 4 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; Fanconi Anemia Pathway; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [O94782](https://www.uniprot.org/uniprotkb/O94782) (Ubiquitin carboxyl-terminal hydrolase 1):

> Negative regulator of DNA damage repair which specifically deubiquitinates monoubiquitinated FANCD2. Also involved in PCNA-mediated translesion synthesis (TLS) by deubiquitinating monoubiquitinated PCNA. Has almost no deubiquitinating activity by itself and requires the interaction with WDR48 to have a high activity.

**Summary**, from NCBI Gene [7398](https://www.ncbi.nlm.nih.gov/gene/7398):

> This gene encodes a member of the ubiquitin-specific processing (UBP) family of proteases that is a deubiquitinating enzyme (DUB) with His and Cys domains. This protein is located in the cytoplasm and cleaves the ubiquitin moiety from ubiquitin-fused precursors and ubiquitinylated proteins. The protein specifically deubiquitinates a protein in the Fanconi anemia (FA) DNA repair pathway. Alternate transcriptional splice variants have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12607) · Entrez [7398](https://www.ncbi.nlm.nih.gov/gene/7398) · UniProt [O94782](https://www.uniprot.org/uniprotkb/O94782) · Ensembl [ENSG00000162607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162607)

## Data

Gene col 8541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8541); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8541]; `tensor/DDL_lfc|DDL_z.npy` [8541]; `embed/gene_vectors.npy` [8541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8541 or target_col == 8541). Every well: [[USP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/USP1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
