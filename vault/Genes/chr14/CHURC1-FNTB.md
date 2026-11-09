---
symbol: "CHURC1-FNTB"
type: "gene"
col: 4696
ensembl_id: "ENSG00000125954"
name: "CHURC1-FNTB readthrough"
location: "14q23.3"
module: 37
arm: "+"
pooled_cpm: 19.68
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CHURC1-FNTB

*CHURC1-FNTB readthrough* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.25× (z +5.6, q 1e-05, up in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 1.30× (z +4.6, q 0.001, up in 15 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.438× (z -15.0, q 0e+00, down in 35 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.789× (z -4.1, q 0.002, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM20]] (+0.60, fdr 1e-05), [[TMEM225B]] (+0.60, fdr 1e-05), [[ZNF814]] (+0.58, fdr 1e-05); moves opposite to [[ACTR3]] (-0.57, fdr 1e-05), [[RBBP7]] (-0.56, fdr 1e-05), [[CHML]] (-0.55, fdr 2e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GFOD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.25×** | +5.6 | 1e-05 | 23/48 (LS 180, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +4.6 | 0.001 | 15/45 (A549, SW 900, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.26×** | +4.2 | 0.003 | 14/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.2 | 0.003 | 9/26 (SW480, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.003 | 8/46 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.0 | 0.005 | 11/41 (LOX-IMVI, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.005 | 16/45 (NCI-H460, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.8 | 0.011 | 9/46 (HOP62, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +3.6 | 0.023 | 12/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.025 | 7/48 (CFPAC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.029 | 8/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.058 | 11/47 (HEC-1-A, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.438×** | -15.0 | 0e+00 | 35/40 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.505×** | -12.0 | 2e-30 | 23/32 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.552×** | -10.0 | 3e-21 | 23/35 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.642×** | -7.7 | 1e-12 | 27/44 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.705×** | -6.3 | 3e-08 | 24/48 (J82, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.713×** | -6.1 | 8e-08 | 23/48 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.795×** | -5.7 | 9e-07 | 21/45 (SW480, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.733×** | -5.4 | 4e-06 | 20/47 (SNU-423, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.789×** | -4.3 | 0.001 | 20/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.791×** | -4.3 | 0.001 | 15/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.791×** | -4.3 | 0.001 | 16/48 (NCI-H1573, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.789×** | -4.1 | 0.002 | 17/47 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.812×** | -3.8 | 0.007 | 14/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.816×** | -3.7 | 0.009 | 10/47 (RKO, KATO III, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.824×** | -3.5 | 0.017 | 6/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.835× | -3.3 | 0.032 | 8/48 (SW 1088, NCI-H661, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.820×** | -3.2 | 0.039 | 6/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 5 µM |  | **0.719×** | -3.1 | 0.044 | 11/42 (COLO 205, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.824×** | -3.1 | 0.044 | 8/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.838× | -2.9 | 0.098 | 8/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0773× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 3 (2 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0770× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 49.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0386× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.369× (z -8.7) ⚠ cell-cycle shift, explains ~59% of this change |
| [[H4 (line)]] | wt | 32.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0762× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 1 | — | [[Bimiralisib (drug)]] 0.05 µM 0.0709× (z -8.7) |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0829× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM20]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TMEM225B]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ZNF814]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[BET1]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZNF264]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[AASDH]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[GUCA1B]] | +0.56 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ZNF766]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NKAP]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LINC00640]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[AKAP10]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CHML]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[APPAT]] | -0.53 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[GFOD1]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[UBE2E3]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SSX2IP]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[IDH3A]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.50 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CEP78]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MFSD14B]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[GNG12]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFOD1]] | B | GFOD1 activity lowers CHURC1-FNTB's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without GFOD1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-50.4, -7.8); signed map (8.9, 3.2). **Vector** length 94.2, 20.1% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.1 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -5.5 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.0 | -15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.2 | -12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -4.1 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.8 | -5.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | CHURC1-FNTB readthrough |
| Locus type | readthrough (other) |
| Location | 14q23.3 — chr14:64,914,485-65,061,803 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100529261](https://www.ncbi.nlm.nih.gov/gene/100529261):

> This locus represents naturally occurring read-through transcription between the neighboring CHURC1 (churchill domain containing 1) and FNTB (farnesyltransferase, CAAX box, beta) on chromosome 14. The read-through transcript produces a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:42960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42960) · Entrez [100529261](https://www.ncbi.nlm.nih.gov/gene/100529261) · Ensembl [ENSG00000125954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125954)

## Data

Gene col 4696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4696); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4696]; `tensor/DDL_lfc|DDL_z.npy` [4696]; `embed/gene_vectors.npy` [4696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4696 or target_col == 4696). Every well: [[CHURC1-FNTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHURC1-FNTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
