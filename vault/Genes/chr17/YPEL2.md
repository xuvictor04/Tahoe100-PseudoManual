---
symbol: "YPEL2"
type: "gene"
col: 10569
ensembl_id: "ENSG00000175155"
name: "yippee like 2"
location: "17q22"
module: 76
arm: "+"
pooled_cpm: 39.51
n_lines_expressing: 47
n_dd_up: 32
n_dd_down: 47
n_dd_up_clean: 25
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 10
direction_downstream: 4
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# YPEL2

*yippee like 2* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.87× (z +10.6, q 1e-23, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (19 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.150× (z -32.2, q 0e+00, down in 44 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.177× (z -15.3, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC28A]] (+0.71, fdr 7e-06), [[AUH]] (+0.67, fdr 8e-06), [[ELF2]] (+0.66, fdr 7e-06); moves opposite to [[ALG8]] (-0.63, fdr 1e-05), [[P2RY11]] (-0.63, fdr 1e-05), [[TAF2]] (-0.62, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); 4 go from it, the strongest it → [[MPST]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +10.6 | 1e-23 | 34/44 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +10.1 | 1e-21 | 33/45 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +9.7 | 4e-20 | 31/45 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +8.8 | 2e-16 | 38/45 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +6.7 | 3e-09 | 26/44 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +6.4 | 1e-08 | 30/46 (NCI-H1792, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.0 | 2e-07 | 22/43 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.95×** | +5.9 | 2e-07 | 22/46 (BT-474, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.35×** | +5.1 | 2e-05 | 20/46 (NCI-H2347, A-172, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.75×** | +5.0 | 4e-05 | 16/46 (LoVo, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.9 | 5e-05 | 16/45 (LS 180, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.5 | 3e-04 | 16/45 (SW48, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.28×** | +4.2 | 0.001 | 14/45 (A-172, HS-578T, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.002 | 15/44 (SNU-1, Panc 03.27, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.27×** | +4.1 | 0.002 | 12/44 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.004 | 9/44 (BT-474, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.006 | 12/45 (LoVo, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.006 | 11/46 (Hs 766T, BT-474, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.16× | +3.7 | 0.007 | 8/45 (NCI-H2030, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.150×** | -32.2 | 0e+00 | 44/44 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.177×** | -15.3 | 0e+00 | 42/44 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.397×** | -15.1 | 0e+00 | 23/32 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.195×** | -14.5 | 1e-45 | 39/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -14.2 | 1e-43 | 29/44 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.224×** | -13.3 | 2e-38 | 38/44 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.227×** | -13.2 | 1e-37 | 42/44 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.504×** | -11.6 | 2e-29 | 27/41 (Panc 03.27, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -10.7 | 5e-25 | 29/42 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.302×** | -10.6 | 1e-24 | 35/44 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.559×** | -9.1 | 4e-18 | 22/36 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -9.1 | 4e-18 | 29/44 (AsPC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.590×** | -9.0 | 1e-17 | 26/44 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.699×** | -8.6 | 3e-16 | 25/45 (hTERT-HPNE, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.604×** | -8.2 | 7e-15 | 28/44 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.431×** | -8.2 | 9e-15 | 38/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.409×** | -7.9 | 7e-14 | 31/42 (RKO, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.619×** | -7.7 | 4e-13 | 31/45 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.647×** | -7.4 | 4e-12 | 27/45 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.524×** | -6.3 | 8e-09 | 25/44 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.678×** | -6.2 | 1e-08 | 25/45 (LoVo, SW48, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -5.6 | 5e-07 | 23/44 (HT-29, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.719×** | -5.3 | 2e-06 | 18/44 (SW1417, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 67.0 | 0 | 13 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.138× (z -16.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -12.9) |
| [[HT-29 (line)]] | alt | 199 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0883× (z -22.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0647× (z -17.7) |
| [[NCI-H2347 (line)]] | alt | 82.5 | 0 | 11 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.174× (z -18.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.121× (z -11.8) |
| [[BT-474 (line)]] | alt | 386 | 2 (1 ⚠) | 7 (6 ⚠) | [[Neratinib (maleate) (drug)]] 0.05 µM 2.29× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 79.4 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.0998× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0891× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.0430× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0399× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -10.2) |
| [[COLO 205 (line)]] | alt | 43.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -13.8) |
| [[SNU-423 (line)]] | alt | 40.8 | 0 | 6 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.136× (z -15.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -10.4) |
| [[LoVo (line)]] | wt | 25.9 | 1 | 4 (1 ⚠) | [[Binimetinib (drug)]] 5 µM 3.09× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -15.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -9.7) |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.135× (z -16.4) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.115× (z -16.2) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 75.7 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.155× (z -14.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -8.6) |
| [[KATO III (line)]] | alt | 35.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0740× (z -17.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -11.5) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 63.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.112× (z -17.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -15.8) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -11.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0820× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[RKO (line)]] | wt | 20.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -9.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.193× (z -8.5) |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.120× (z -11.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.199× (z -8.5) |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.05 µM 0.0595× (z -10.9) |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -12.2) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.185× (z -14.4) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -10.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.134× (z -11.2) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.145× (z -10.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0469× (z -11.2) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HEC-1-A (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0757× (z -17.1) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -8.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.1) |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -8.7) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.147× (z -10.0) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.191× (z -8.7) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.106× (z -11.0) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 18.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0772× (z -9.8) |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC28A]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[AUH]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[ELF2]] | +0.66 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[GALM]] | +0.66 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[RAB40B]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | same gene group |
| [[YPEL3]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 | same gene group |
| [[SPSB3]] | +0.64 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[HDAC5]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MED30]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RALBP1]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[THRA]] | +0.63 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[STRN]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[P2RY11]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[TAF2]] | -0.62 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.62 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.62 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[RNASEH1]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MCM3AP]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[DUS2]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[PIGW]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AVEN]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers YPEL2's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.6% of all compounds | 0.028 | ⚠ off-target possible; 5 compounds |
| [[ATP8B1]] | B | ATP8B1 activity raises YPEL2's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without ATP8B1 | 0.029 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ELF3]] | B | ELF3 activity raises YPEL2's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without ELF3 | 0.029 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[ERBB3]] | B | ERBB3 activity raises YPEL2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 1.92× lower at baseline in the lines without ERBB3 | 0.030 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[ENPP5]] | B | ENPP5 activity raises YPEL2's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without ENPP5 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[TJP3]] | B | TJP3 activity raises YPEL2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TJP3 | 0.075 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[NR3C2]] | B | NR3C2 activity raises YPEL2's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without NR3C2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[NCMAP]] | B | NCMAP activity raises YPEL2's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without NCMAP | 0.083 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[GRB7]] | B | GRB7 activity raises YPEL2's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without GRB7 | 0.099 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[BMF]] | C | BMF activity raises YPEL2's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without BMF | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPST]] | C | YPEL2 activity raises MPST's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without YPEL2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |
| [[INSR]] | C | YPEL2 activity raises INSR's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without YPEL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |
| [[HDAC5]] | C | YPEL2 activity raises HDAC5's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without YPEL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |
| [[MAPK3]] | C | YPEL2 activity raises MAPK3's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.26× lower at baseline in the lines without YPEL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.8, -46.4); signed map (-17.9, 9.4). **Vector** length 135, 41.4% of its response variance represented; |z| ≥ 3 in 1,528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.7 | +6.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +8.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.9 | -32.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.3 | -15.3 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -13.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.2 | -13.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.9 | -14.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | yippee like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:59,331,655-59,401,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG4 |
| Gene groups (HGNC) | Yippee like family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q96QA6](https://www.uniprot.org/uniprotkb/Q96QA6) carries no function annotation.

**Summary**, from NCBI Gene [388403](https://www.ncbi.nlm.nih.gov/gene/388403):

> Predicted to enable metal ion binding activity. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18326) · Entrez [388403](https://www.ncbi.nlm.nih.gov/gene/388403) · UniProt [Q96QA6](https://www.uniprot.org/uniprotkb/Q96QA6) · Ensembl [ENSG00000175155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175155)

## Data

Gene col 10569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10569); `tables/drug_effects.parquet` (100 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10569]; `tensor/DDL_lfc|DDL_z.npy` [10569]; `embed/gene_vectors.npy` [10569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10569 or target_col == 10569). Every well: [[YPEL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YPEL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
